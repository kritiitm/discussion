### Post 330
**Post URL**: /t/tds-official-project1-discrepencies/171141/330
- **ID**: 616101
- **Author**: Tushar Jalan  (23f2003751)
- **Created At**: 2025-04-06T13:29:44.621Z
- **Reply To**: Post 316 (, )
- **Content**:  
  <strong>Things i have done for my project to work locally:</strong>
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>git clone &lt;your repo url&gt;</code>
</blockquote>
</aside>
cloned my repo which looked like this after cloning(ignore those green dots)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png" data-download-href="/uploads/short-url/bCYFeHxVzBnl2fAh3CxgzgJ8Xdw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png" alt="image" data-base62-sha1="bCYFeHxVzBnl2fAh3CxgzgJ8Xdw" width="205" height="88"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">274×118 2.87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
All the files are  in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
Keep datagen.py and evaluate.py in same folder
</blockquote>
</aside>
when i do this( <img src="https://emoji.discourse-cdn.com/google/down_arrow.png?v=14" title=":down_arrow:" class="emoji" alt=":down_arrow:" loading="lazy" width="20" height="20">) i get this error
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>docker build -t &lt;your image name&gt;</code>
</blockquote>
</aside>
<pre><code class="lang-auto">PS D:\TDS_Project_1\tds-project-1&gt; docker build -t "tushar2k5/tds-project-1"                                                                 
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build
</code></pre>
Instead,in order to run the docker image successfully  we have to do either of the two things(taken help from chatgpt <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">):<br>
1)
<pre><code class="lang-auto">Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1
</code></pre>
<strong>OR</strong><br>
2)
<pre><code class="lang-auto">Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .
</code></pre>
<em>Both the things work for me</em>(<img src="https://emoji.discourse-cdn.com/google/up_arrow.png?v=14" title=":up_arrow:" class="emoji" alt=":up_arrow:" loading="lazy" width="20" height="20">)
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt;</code>
</blockquote>
</aside>
<pre><code class="lang-auto">docker run -e AIPROXY_TOKEN=i.am.still.noob.inTDS -p 8000:8000 tushar2k5/tds-project-1
</code></pre>
Done this(can’t leak my token,already many students stolen it from my project-2🤦‍♂️)
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000</code>
</blockquote>
</aside>
<pre><code class="lang-auto">uv run evaluate.py --email=23f2003751@ds.study.iitm.ac.in --token_counter 1 --external_port 8000 
</code></pre>
Done this to evaluate my project
Any finally the main part (DRUM ROLLS <img src="https://emoji.discourse-cdn.com/google/drum.png?v=14" title=":drum:" class="emoji" alt=":drum:" loading="lazy" width="20" height="20">,not this one <img src="https://emoji.discourse-cdn.com/google/oil_drum.png?v=14" title=":oil_drum:" class="emoji" alt=":oil_drum:" loading="lazy" width="20" height="20"> (IUKUK))
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png" data-download-href="/uploads/short-url/A19AAp90vJqY6Tc8TKnucEVq8qg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png" alt="image" data-base62-sha1="A19AAp90vJqY6Tc8TKnucEVq8qg" width="690" height="143" data-dominant-color="232323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1462×305 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<strong>THATS 6/25</strong>
Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png" data-download-href="/uploads/short-url/cguFlhUIw1ujkDBstIwdfq9uP3T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png" alt="image" data-base62-sha1="cguFlhUIw1ujkDBstIwdfq9uP3T" width="686" height="141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">686×141 5.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Hopping to get a response from you guys,<br>
Thanks a lot(wrote this much for first time for any course)<br>
(PS:This course has some special place in my heart <img src="https://emoji.discourse-cdn.com/google/heart.png?v=14" title=":heart:" class="emoji" alt=":heart:" loading="lazy" width="20" height="20">)<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a>
- **Reactions**: heart (1)
- **Post Number**: 330

