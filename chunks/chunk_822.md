### Post 295
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/295
- **ID**: 594984
- **Author**: Arulvadivelan V (23f2005419)
- **Created At**: 2025-02-14T14:19:40.681Z
- **Reply To**: Post 292 (Daksh Agarwal, daksh76)
- **Content**:  
  <pre><code class="lang-auto">def format_with_prettier(file_path:str, prettier_version:str):
    if file_path and os.path.exists(file_path):
        print('Path exisit - will perform prettier')
        subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])
    else:
        raise FileNotFoundError()
</code></pre>
This is my code
- **Reactions**: None
- **Post Number**: 295

