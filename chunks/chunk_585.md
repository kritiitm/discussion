### Post 58
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/58
- **ID**: 590523
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-04T09:04:40.260Z
- **Content**:  
  <aside class="onebox githubblob" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md">
  <header class="source">

      <a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md"># TDS-Project1-Ollama_FastAPI-
## Info
- Create codespaces on main or evalution script branch
Use history.txt to get sqlite to version 3.45.3 into bash session 
   - 64  export PATH=/opt/conda/bin:$PATH
   - 65  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
   - 66  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"

- cd to latest_ai_development and run cmd [ crewai run] which set up server 
- Then in a separate bash terminal run "python evaluate.py" 
- also make sure to enter openai or sanand api key in crew.py

# Simple history of commands
1. Terminal 1 
    - 1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 2  export PATH=/opt/conda/bin:$PATH
    - 3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    - 4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 5  cd latest_ai_development/
    - 7  pip install crewai crewai-tools
</code></pre>



  This file has been truncated. <a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

My take on autonomous agents. Limited by model capabilities to some extent. Will use function calling hence forth but here is a quick look at using crewai for agent tasks.
- **Reactions**: None
- **Post Number**: 58

