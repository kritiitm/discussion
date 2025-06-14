### Post 72
**Post URL**: /t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/72
- **ID**: 582264
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-01-20T07:26:25.067Z
- **Reply To**: Post 70 (Rohit Kumar , Rohitkumar7463)
- **Content**:  
  <a class="mention" href="/u/rohitkumar7463">@Rohitkumar7463</a> <a class="mention" href="/u/23f2003845">@23f2003845</a>
If you are on Windows Powershell<br>
Then instead of <code>sha256sum</code> you can simply use <code>Get-FileHash</code>
Send the output of the <code>npx -y prettier@3.4.2 README.md</code> to a text file eg. <code>output.txt</code> and then use <code>Get-FileHash</code> on powershell with the <code>output.txt</code> and it will use sha256 by default and give you the exact same output.<br>
You might be able to pipe the data directly to <code>Get-FileHash</code> but I have not tried direct piping. The above method works guaranteed.
Kind regards
- **Reactions**: None
- **Post Number**: 72

