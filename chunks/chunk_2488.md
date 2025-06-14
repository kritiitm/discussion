### Post 168
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/168
- **ID**: 612867
- **Author**: Saransh Saini (Saransh_Saini)
- **Created At**: 2025-03-29T14:57:58.480Z
- **Reply To**: Post 159 (Pradeep Mondal, 21f2000709)
- **Content**:  
  This is a basic prototype function we would be using to send requests to your URL.
<pre data-code-wrap="python"><code class="lang-python">def run(question, file_path):
    url = "http://127.0.0.1:8080/api"
    questions = {'question': question}
    files = [
        ('file', open("abcd.zip", 'rb')),
        ('file', open("dcba.img", 'rb'))
    ]
    response = requests.post(url, data=questions, files=files)
    return response
</code></pre>
or
<pre data-code-wrap="curl"><code class="lang-curl">curl -X POST "http://127.0.0.1:8080/api" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question" \
  -F "file=@abcd.zip" \
  -F "file=@dcba.img"
</code></pre>
<em><strong>NOTE</strong>: This is not the evaluation script.</em>
- **Reactions**: None
- **Post Number**: 168

