### Post 71
**Post URL**: /t/tds-official-project1-discrepencies/171141/71
- **ID**: 612520
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-03-29T07:51:29.081Z
- **Reply To**: Post 57 (Shashannk, 23f2003413)
- **Content**:  
  We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.
Line number 81 of your app.py
<code>subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)</code>
which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.
- **Reactions**: None
- **Post Number**: 71

