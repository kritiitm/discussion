### Post 196
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/196
- **ID**: 594351
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-02-13T07:40:40.412Z
- **Reply To**: Post 149 (Shaurya Sharad Shukla, TRIGON)
- **Content**:  
  After submitting docker image through, it will be pulled and our token will be used.
Things to be checked at your end.<br>
1.<code> podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME</code> works fine<br>
2.  Above command will start 8000 server so use evaluate.py to test if things are working as expected.
Kind regards.<br>
Jivraj
- **Reactions**: None
- **Post Number**: 196

