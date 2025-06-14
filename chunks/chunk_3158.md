### Post 94
**Post URL**: /t/tds-official-project1-discrepencies/171141/94
- **ID**: 612599
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-03-29T09:09:48.134Z
- **Reply To**: Post 93 (Achuthan M, 22f3002867)
- **Content**:  
  That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.
Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.
- **Reactions**: None
- **Post Number**: 94

