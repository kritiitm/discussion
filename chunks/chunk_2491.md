### Post 171
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/171
- **ID**: 612973
- **Author**: Pradeep Mondal (21f2000709)
- **Created At**: 2025-03-29T16:35:24.959Z
- **Reply To**: Post 168 (, )
- **Content**:  
  <aside class="quote group-ds-students" data-username="Saransh_Saini" data-post="168" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png" class="avatar"> Saransh_Saini:</div>
<blockquote>
This is a basic prototype function we would be using to send requests to your URL.
<pre><code class="lang-auto">def run(question, file_path):
    url = "http://127.0.0.1:8080/api"
    questions = {'question': question}
    files = [
        ('file', open("abcd.zip", 'rb')),
        ('file', open("dcba.img", 'rb'))
    ]
    response = requests.post(url, data=questions, files=files)
    return response
</code></pre>
</blockquote>
</aside>
I couldn’t find this function on the Project Doc and I made the project based on the curl function calling.
<aside class="quote group-ds-students" data-username="Saransh_Saini" data-post="168" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png" class="avatar"> Saransh_Saini:</div>
<blockquote>
<pre><code class="lang-auto">curl -X POST "http://127.0.0.1:8080/api" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question" \
  -F "file=@abcd.zip" \
  -F "file=@dcba.img"
</code></pre>
</blockquote>
</aside>
At this moment it can’t be changed as I am occupied with other things. Please keep the question parameter as “question” and file parameter as “file” in the evaluation which is on the Project 2 page and the content type as multipart/form-data.
To clarify if I can handle any one of these 2 methods, I will be fine?
Edit:<br>
Just now discovered that the field names are indeed “question” and “file” only in both the cases. Sorry for the oversight.
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
- **Reactions**: None
- **Post Number**: 171

