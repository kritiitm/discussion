### Post 130
**Post URL**: /t/tds-official-project1-discrepencies/171141/130
- **ID**: 613369
- **Author**: RAJ K BOOPATHI (23ds2000092)
- **Created At**: 2025-03-30T10:31:12.160Z
- **Content**:  
  Hi,
For Tasks A8, A9 &amp; A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.
For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK
<pre><code class="lang-auto">ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO:     172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

</code></pre>
Similarly for task B2.
<pre><code class="lang-auto">INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO:     172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK
</code></pre>
For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.
For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?<br>
Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8
- **Reactions**: None
- **Post Number**: 130

