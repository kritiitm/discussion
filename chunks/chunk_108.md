### Post 96
**Post URL**: /t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/96
- **ID**: 584707
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-01-25T05:40:24.502Z
- **Reply To**: Post 85 (Arnav Raj , 23f3002537)
- **Content**:  
  Hi Arnav,
I tried your script on your dataset.<br>
Problem might be you are not executing <code>grep . * | LC_ALL=C sort | sha256sum</code> in correct directory, you would need to execute it from <code>all_files</code> directory also there should not be any extra file other than that gets generated.
- **Reactions**: +1 (1)
- **Post Number**: 96

