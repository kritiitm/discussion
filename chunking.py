import os
import re

# Initialize logs
error_log = []
debug_log = []

# Input and output paths
input_file = "forum_posts.md"
output_dir = "chunks"
os.makedirs(output_dir, exist_ok=True)

# Read the Markdown file
try:
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()
except FileNotFoundError:
    error_log.append(f"Input file {input_file} not found")
    print(f"Error: Input file {input_file} not found")
    with open("chunk_error_log.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(error_log))
    exit(1)

# Split content into chunks based on '### Post' header
post_pattern = r'^### Post \d+\n'
posts = re.split(post_pattern, markdown_content, flags=re.MULTILINE)
post_headers = re.findall(post_pattern, markdown_content, flags=re.MULTILINE)

# Skip the file header (e.g., '# Forum Posts')
if posts and not posts[0].strip().startswith("**Post URL**"):
    posts = posts[1:]
    post_headers = post_headers[:len(posts)]

# Process each post
chunk_count = 0
for i, (header, post_content) in enumerate(zip(post_headers, posts), 1):
    if not post_content.strip():
        debug_log.append(f"Skipping empty post section {i}")
        continue
    
    full_post = header + post_content
    
    if not full_post.lstrip(header).strip().startswith("**Post URL**:"):
        error_log.append(f"Post {i} missing or misplaced **Post URL**")
        print(f"Error: Post {i} missing or misplaced **Post URL**")
        continue
    
    chunk_filename = os.path.join(output_dir, f"chunk_{str(chunk_count + 1).zfill(3)}.md")
    try:
        with open(chunk_filename, "w", encoding="utf-8") as f:
            f.write(full_post)
        chunk_count += 1
        debug_log.append(f"Created chunk {chunk_filename} for Post {i}")
    except Exception as e:
        error_log.append(f"Failed to write chunk {chunk_filename}: {str(e)}")
        print(f"Error writing chunk {chunk_filename}: {str(e)}")

with open("chunk_error_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(error_log))
with open("chunk_debug_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(debug_log))

print(f"Chunking complete. {chunk_count} chunks created in '{output_dir}'.")
print(f"Error log written to 'chunk_error_log.txt'. {len(error_log)} issues encountered.")
print(f"Debug log written to 'chunk_debug_log.txt'. {len(debug_log)} entries logged.")