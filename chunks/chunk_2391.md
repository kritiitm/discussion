### Post 71
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/71
- **ID**: 608793
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-03-20T10:43:34.757Z
- **Reply To**: Post 68 (, )
- **Content**:  
  <aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
The data file sent to the api will always be in the <strong>requester’s</strong> local machine. When the api server receives the request, the file will be in binary format?
Or
Sometimes the api server receives the file in byte and some times, it will recieve a link like this : <a href="https://exam.sanand.workers.dev/shapes.png" rel="noopener nofollow ugc">https://exam.sanand.workers.dev/shapes.png</a>
</blockquote>
</aside>
file format will be exactly same as corresponding GA.
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
<pre><code class="lang-auto">"&lt;table&gt;\n&lt;thead&gt;\n&lt;tr&gt;\n&lt;th&gt;Col 1&lt;/th&gt;\n&lt;th&gt;Col 2&lt;/th&gt;\n&lt;/tr&gt;\n&lt;/thead&gt;\n&lt;tbody&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 1, Col1&lt;/td&gt;\n&lt;td&gt;Row 1 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;tr&gt;\n&lt;td&gt;Row 2, Col 1&lt;/td&gt;\n&lt;td&gt;Row 2 Col 2&lt;/td&gt;\n&lt;/tr&gt;\n&lt;/tbody&gt;\n&lt;/table&gt;
</code></pre>
</blockquote>
</aside>
This is correct html table format.
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
Should it just be the answer or should it be the html string which will have the disabled block enabled and also the answer string sitting inside the block
</blockquote>
</aside>
It will be just answer.
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
Some questions have more than one file. For example, the last question of GA5, it has a png file in this link <a href="https://exam.sanand.workers.dev/jigsaw.webp" rel="noopener nofollow ugc">https://exam.sanand.workers.dev/jigsaw.webp</a> and a table.
In this case, how will the curl request be? Is it some thing like this
<pre><code class="lang-auto">curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question text" \
  -F "file= Image file" \
  -F "file= table file/ string" 
</code></pre>
</blockquote>
</aside>
In last question of GA5 there is only one file(image), table is not coming through file, it will be kept same for project2.
<aside class="quote group-ds-students" data-username="23f2000573" data-post="68" data-topic="169029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png" class="avatar"> 23f2000573:</div>
<blockquote>
Will the CORS headers asked in the question be the same or can it be different?
</blockquote>
</aside>
I didn’t get this question, could you point to exact question?
- **Reactions**: None
- **Post Number**: 71

