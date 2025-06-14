### Post 141
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/141
- **ID**: 594043
- **Author**: Durga Prasad (22f3001307)
- **Created At**: 2025-02-12T07:12:02.257Z
- **Reply To**: Post 139 (Durga Prasad, 22f3001307)
- **Content**:  
  Hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>,
I followed what you taught in Feb 11 session and tried implementing task A1. My understanding is once i run the subprocess, datagen.py file should be run and /data folder should be created in the project folder. But it is not happening to me. I am getting the following error
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/datagen4COEF3.py", line 284, in &lt;module&gt;
    os.makedirs(config["root"], exist_ok=True)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "&lt;frozen os&gt;", line 227, in makedirs
OSError: [Errno 30] Read-only file system: '/data'
</code></pre>
If i can’t automate this process, i don’t see the point writing code for other tasks. Can anyone help me solving this error?
- **Reactions**: None
- **Post Number**: 141

