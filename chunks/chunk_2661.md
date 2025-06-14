### Post 341
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/341
- **ID**: 615157
- **Author**: Vicky Kumar (Algsoch)
- **Created At**: 2025-04-04T06:37:32.871Z
- **Content**:  
  :
<hr>
<h1><a name="p-615157-from-problem-to-platform-building-vicky-a-smart-data-science-assistant-for-tds-iit-madras-1" class="anchor" href="#p-615157-from-problem-to-platform-building-vicky-a-smart-data-science-assistant-for-tds-iit-madras-1"></a><img src="https://emoji.discourse-cdn.com/google/graduation_cap.png?v=14" title=":graduation_cap:" class="emoji" alt=":graduation_cap:" loading="lazy" width="20" height="20"> From Problem to Platform: Building “Vicky” – A Smart Data Science Assistant for TDS @ IIT Madras</h1>
<img src="https://emoji.discourse-cdn.com/google/rocket.png?v=14" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"> <strong>Project Demo Website</strong>: <a href="https://app.algsoch.tech" rel="noopener nofollow ugc">https://app.algsoch.tech</a>
During our college course <em>Tool for Data Science (TDS)</em> at <strong>IIT Madras</strong>, we were tasked with a challenging but exciting project: <strong>to build a platform that can take in natural language questions and execute corresponding solutions through an API</strong>.
<h2><a name="p-615157-the-mission-2" class="anchor" href="#p-615157-the-mission-2"></a><img src="https://emoji.discourse-cdn.com/google/brain.png?v=14" title=":brain:" class="emoji" alt=":brain:" loading="lazy" width="20" height="20"> The Mission:</h2>
Create a tool that behaves like a <strong>chatbot</strong>, accepts <strong>user queries (text or file-based)</strong> via <strong>web or API</strong>, processes them intelligently, <strong>executes the appropriate code</strong>, and returns accurate results—like a real data science assistant.
<hr>
<h2><a name="p-615157-the-journey-from-fails-to-final-3" class="anchor" href="#p-615157-the-journey-from-fails-to-final-3"></a><img src="https://emoji.discourse-cdn.com/google/counterclockwise_arrows_button.png?v=14" title=":counterclockwise_arrows_button:" class="emoji" alt=":counterclockwise_arrows_button:" loading="lazy" width="20" height="20"> The Journey: From Fails to Final</h2>
At first, the natural choice was to try <strong>LLM agents</strong>—they sounded magical. But in real-world usage, they were slow, unreliable, and lacked precision. Most failed to parse or execute even moderately dynamic queries. <img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20">
Then I thought—what if I manually mapped questions and answers using a <strong>static JSON structure</strong>? That quickly broke when users passed <strong>different parameters, different files</strong>, or queried in <strong>non-standard formats</strong> like “code -s” or “code -v”.
The next idea: write <strong>individual Python scripts per question</strong> from our Graded Assignments (GA1–GA5). But that lacked flexibility and reusability. Creating multiple files became unmanageable and non-scalable. <img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20">
<hr>
<h2><a name="p-615157-the-breakthrough-dynamic-function-mapping-4" class="anchor" href="#p-615157-the-breakthrough-dynamic-function-mapping-4"></a><img src="https://emoji.discourse-cdn.com/google/wrench.png?v=14" title=":wrench:" class="emoji" alt=":wrench:" loading="lazy" width="20" height="20"> The Breakthrough: Dynamic Function Mapping</h2>
After multiple iterations and failed prototypes, I finally found the right architecture:
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Centralized engine in <code>vicky_server.py</code><br>
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Uses <strong>regex-based pattern matching</strong> to detect question types, extract parameters, and identify the correct solution<br>
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Each solution is a structured Python function like <code>ga1_first_solution(query=None)</code><br>
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Supports dynamic parameter injection, command-line variations, file-based queries, and more<br>
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Acts like a <strong>mini compiler for data science tools</strong>
<hr>
<h2><a name="p-615157-presenting-vicky-the-mini-chatbot-for-tds-5" class="anchor" href="#p-615157-presenting-vicky-the-mini-chatbot-for-tds-5"></a><img src="https://emoji.discourse-cdn.com/google/globe_with_meridians.png?v=14" title=":globe_with_meridians:" class="emoji" alt=":globe_with_meridians:" loading="lazy" width="20" height="20"> Presenting Vicky – The Mini Chatbot for TDS <img src="https://emoji.discourse-cdn.com/google/fire.png?v=14" title=":fire:" class="emoji" alt=":fire:" loading="lazy" width="20" height="20"></h2>
Vicky is a <strong>smart, modular chatbot</strong> built specifically for <strong>Tool for Data Science at IIT Madras</strong>. It’s packed with real functionality—not just templates.
<h3><a name="p-615157-key-features-6" class="anchor" href="#p-615157-key-features-6"></a>Key Features:</h3>
<img src="https://emoji.discourse-cdn.com/google/brain.png?v=14" title=":brain:" class="emoji" alt=":brain:" loading="lazy" width="20" height="20"> <strong>Graded Assignment Solver</strong><br>
Handles dynamic, real-world questions from GA1 to GA5 like:
<ul>
<li><code>code -s</code> / <code>code -v</code> → VS terminal commands</li>
<li>Create FastAPI API for CSV with filtering/searching</li>
<li>GitHub automation: repo creation, GitHub Actions setup</li>
<li>Data cleaning, scraping from IMDb, image compression</li>
</ul>
<img src="https://emoji.discourse-cdn.com/google/open_file_folder.png?v=14" title=":open_file_folder:" class="emoji" alt=":open_file_folder:" loading="lazy" width="20" height="20"> <strong>File Upload with Query Matching</strong><br>
Users can upload a file (CSV, JSON, Excel) and ask file-specific queries. The system understands context and dynamically links the query to the uploaded file.
<img src="https://emoji.discourse-cdn.com/google/globe_showing_europe_africa.png?v=14" title=":globe_showing_europe_africa:" class="emoji" alt=":globe_showing_europe_africa:" loading="lazy" width="20" height="20"> <strong>HTML Viewer + Base64 Decoder</strong>
<ul>
<li>View any website in rendered &amp; source format using CORS proxy</li>
<li>Upload Base64 string → Get original image back</li>
</ul>
<img src="https://emoji.discourse-cdn.com/google/robot.png?v=14" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> <strong>Webhooks Integration</strong>
<ul>
<li>Live notifications via <strong>Discord</strong> &amp; <strong>Slack</strong> whenever <code>/api</code> endpoints are accessed</li>
<li>Monitors <strong>server status (online/offline)</strong> and sends real-time updates</li>
</ul>
<img src="https://emoji.discourse-cdn.com/google/spouting_whale.png?v=14" title=":spouting_whale:" class="emoji" alt=":spouting_whale:" loading="lazy" width="20" height="20"> <strong>LLM Download + Auto Tunneling</strong>
<ul>
<li>Downloads LLaMA models</li>
<li>Dynamically finds available ports</li>
<li>Creates and exposes tunneled endpoints</li>
</ul>
<img src="https://emoji.discourse-cdn.com/google/chart_increasing.png?v=14" title=":chart_increasing:" class="emoji" alt=":chart_increasing:" loading="lazy" width="20" height="20"> <strong>Live Web UI at <a href="https://app.algsoch.tech" rel="noopener nofollow ugc">app.algsoch.tech</a></strong>
<ul>
<li>Ask any TDS question</li>
<li>Upload and query with files</li>
<li>Image decoder</li>
<li>Graded assignment slider navigation</li>
<li>HTML viewer</li>
<li>API health status</li>
</ul>
<hr>
<h2><a name="p-615157-built-with-7" class="anchor" href="#p-615157-built-with-7"></a><img src="https://emoji.discourse-cdn.com/google/man_technologist.png?v=14" title=":man_technologist:" class="emoji" alt=":man_technologist:" loading="lazy" width="20" height="20"> Built With:</h2>
<ul>
<li><strong>FastAPI</strong> for blazing fast APIs</li>
<li><strong>Regex &amp; Pattern Matching</strong> for dynamic input detection</li>
<li><strong>GitHub Copilot</strong> + my Python debugging and architectural thinking</li>
<li>Full webhook and status monitoring system</li>
<li>Modular backend (<code>vicky_server.py</code>) and web frontend (<code>vicky_app.py</code>)</li>
</ul>
I want to extend a huge thank you to <a class="mention" href="/u/s.anand">@s.anand</a> for their guidance on this project. I’ve learned what prompt engineering is and how we can leverage large language models (LLMs). One interesting takeaway is that while these technologies won’t replace our jobs—especially for those who understand programming—they will create new job opportunities instead.<br>
Now I am capable of how fastapi work and more things and how to structure code and how to design code and most important what to think for project
- **Reactions**: heart (4)
- **Post Number**: 341

