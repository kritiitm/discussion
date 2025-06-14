import os
import json
from datetime import datetime
import pytz


markdown = "# Forum Posts (January 1, 2025 - April 14, 2025)\n\n"


error_log = []
debug_log = []


start_date = datetime(2025, 1, 1, tzinfo=pytz.UTC)
end_date = datetime(2025, 4, 14, 23, 59, 59, tzinfo=pytz.UTC)

for root, dirs, files in os.walk("sc"):
    json_files = [f for f in files if f.endswith(".json")]
    

    topics = {}
    
    # Process each JSON file
    for file in json_files:
        file_path = os.path.join(root, file)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                posts = json.load(f)
                # Ensure posts is a list
                if not isinstance(posts, list):
                    error_log.append(f"Skipping {file}: Expected a list of posts")
                    print(f"Skipping {file}: Expected a list of posts")
                    continue
                
                # Group posts by topic_id
                for post in posts:
                    topic_id = post.get("topic_id")
                    # Skip posts with None or invalid topic_id
                    if topic_id is None or not isinstance(topic_id, (int, str)):
                        error_log.append(f"Skipping post in {file}: Invalid topic_id {topic_id}")
                        print(f"Skipping post in {file}: Invalid topic_id {topic_id}")
                        continue
                    

                    created_at_str = post.get("created_at")
                    try:

                        created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))

                        if created_at.tzinfo is None:
                            created_at = created_at.replace(tzinfo=pytz.UTC)
                        
                        # Log for debugging
                        debug_log.append(f"Post in {file}: created_at={created_at}, start_date={start_date}, end_date={end_date}")
                        
                        # Check if post is within date range
                        if not (start_date <= created_at <= end_date):
                            debug_log.append(f"Skipping post in {file}: created_at {created_at} outside range {start_date} to {end_date}")
                            print(f"Skipping post in {file}: created_at {created_at} outside range")
                            continue
                    except (ValueError, TypeError) as e:
                        error_log.append(f"Skipping post in {file}: Invalid created_at {created_at_str}: {str(e)}")
                        print(f"Skipping post in {file}: Invalid created_at {created_at_str}: {str(e)}")
                        continue
                    
                    if topic_id not in topics:
                        topics[topic_id] = {
                            "slug": post.get("topic_slug", "unknown-topic"),
                            "posts": []
                        }
                    topics[topic_id]["posts"].append(post)
            except json.JSONDecodeError as e:
                error_log.append(f"Error decoding JSON in {file}: {str(e)}")
                print(f"Error decoding JSON in {file}: {str(e)}")
                continue
    
    # Sort topics by topic_id (convert to string for safety if mixed types exist)
    for topic_id in sorted(topics.keys(), key=lambda x: str(x)):
        topic = topics[topic_id]
        slug = topic["slug"].replace("-", " ").title()
        markdown += f"## Topic: {slug}\n"
        markdown += f"**Topic ID**: {topic_id}\n"
        markdown += f"**Topic Slug**: {topic['slug']}\n\n"
        
        # Sort posts by post_number
        sorted_posts = sorted(topic["posts"], key=lambda x: x.get("post_number", 0))
        
        for post in sorted_posts:
            markdown += f"### Post {post['post_number']}\n"
            markdown += f"**Post URL**: {post['post_url']}\n"
            markdown += f"- **ID**: {post['id']}\n"
            markdown += f"- **Author**: {post['name']} ({post['username']})\n"
            markdown += f"- **Created At**: {post['created_at']}\n"
            if post.get("reply_to_post_number"):
                reply_user = post.get("reply_to_user", {})
                markdown += f"- **Reply To**: Post {post['reply_to_post_number']} ({reply_user.get('name', '')}, {reply_user.get('username', '')})\n"
            markdown += f"- **Content**:  \n  {post['cooked'].replace('<p>', '').replace('</p>', '')}\n"
            reactions = ', '.join([f"{r['id']} ({r['count']})" for r in post.get('reactions', [])]) if post.get('reactions') else 'None'
            markdown += f"- **Reactions**: {reactions}\n"
            markdown += f"- **Post Number**: {post['post_number']}\n\n"

# Write to output Markdown file
with open("forum_posts.md", "w", encoding="utf-8") as f:
    f.write(markdown)

# Write error log to a file
with open("error_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(error_log))

# Write debug log to a file
with open("debug_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(debug_log))

print("Markdown file 'forum_posts.md' generated successfully.")
print(f"Error log written to 'error_log.txt'. {len(error_log)} issues encountered.")
print(f"Debug log written to 'debug_log.txt'. {len(debug_log)} entries logged.")