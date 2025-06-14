### Post 400
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/400
- **ID**: 595380
- **Author**: Tanush Tambe (22f3002248)
- **Created At**: 2025-02-15T12:23:41.857Z
- **Reply To**: Post 398 (Nelson Jochim DSouza, Nelson)
- **Content**:  
  you have to give the <code>AIPROXY_TOKEN</code> to the evaluate.py by either<br>
bash - <code>export AIPROXY_TOKEN="your token"</code><br>
or<br>
powershell - <code>$env:AIPROXY_TOKEN="your token"</code><br>
the evaluate.py file takes the token to send request to embedding end point for processing.<br>
so you have to set <code>AIPROXY_TOKEN</code> in both terminals<br>
i.e. app.py and evaluate.py teminals
- **Reactions**: None
- **Post Number**: 400

