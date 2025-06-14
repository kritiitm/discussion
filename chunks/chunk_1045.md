### Post 518
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/518
- **ID**: 595860
- **Author**: Aditya Kumar Sahu (Aditya_Sahu)
- **Created At**: 2025-02-16T10:15:40.611Z
- **Reply To**: Post 506 (Kabir Vyas, Kabir1203)
- **Content**:  
  Use following as first parameter of <code>subprocess.run()</code> to create <code>data/</code> directory inside your project instead of C: drive
<pre data-code-wrap="python"><code class="lang-python">["uv", "run", script_url, user_email, "--root", "./data"]
</code></pre>
Also, you don’t need to download to script, you can directly run it from the url.
- **Reactions**: heart (1)
- **Post Number**: 518

