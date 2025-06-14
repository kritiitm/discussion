### Post 484
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/484
- **ID**: 595668
- **Author**: Abhigyan Das (abhigyandsa)
- **Created At**: 2025-02-15T18:44:11.463Z
- **Content**:  
  On my system evaulate.py is throwing an error on A2 trying to execute npx on format.md before the llm is even invoked. However running the command directly on the command line works.
evaluate.py:<br>
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A2 failed: Command ‘[‘npx’, ‘prettier@3.4.2’, ‘–stdin-filepath’, ‘data/format.md’]’ returned non-zero exit status 2.
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A2 FAILED
bash:<br>
npx prettier@3.4.2 --stdin-filepath data/format.md
bash works as expected. Can someone help?
- **Reactions**: None
- **Post Number**: 484

