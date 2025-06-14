### Post 440
**Post URL**: /t/tds-official-project1-discrepencies/171141/440
- **ID**: 617017
- **Author**: D HARICHARAN  (Haricharan)
- **Created At**: 2025-04-08T13:24:46.118Z
- **Reply To**: Post 433 (Carlton D'Silva, carlton)
- **Content**:  
  Respected Sir,
<ul>
<li>Yes Sir, I said the same,  <code>.env</code> was not able to be uploaded to repo as .env file was not allowed to be uploaded</li>
<li>when we download the repository it doesn’t have the <code>.env</code> file,</li>
<li>for docker image to build we need to add <code>.env</code> with <code>AIPROXY_TOKEN</code></li>
<li>after that docker image will build, I had given about this in previous message</li>
<li>As you said Sir that you will use separate <code>AIPROXY_TOKEN</code>…you can put that in <code>.env</code> file and build the docker image</li>
<li>after that Sir its optional to pass <code>AIPROXY_TOKEN</code> again while running the docker Image</li>
<li>just the <code>.env</code> file required, even without token in that it will work as project has support for both AIPROXY token in .env file and as environment variable</li>
</ul>
and when I uploaded to repository the .env file was not allowed to upload so had submitted that way, I actually forgot to add step for running the docker image in the previous message, the steps which I used:
<pre><code class="lang-auto">git clone https://github.com/23f2001390/llmagent.git
</code></pre>
adding <code>.env</code> with AIPROXY token and replacing <code>evaluate.py</code> and <code>datagen.py</code> with new ones according to test environment
<pre><code class="lang-auto">docker build -t llm-agent .
</code></pre>
<pre><code class="lang-auto">docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent
</code></pre>
and in another terminal
<pre><code class="lang-auto">uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000
</code></pre>
Thank you<br>
Kind regards
- **Reactions**: None
- **Post Number**: 440

