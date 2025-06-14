### Post 434
**Post URL**: /t/tds-official-project1-discrepencies/171141/434
- **ID**: 616847
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-08T06:01:28.431Z
- **Reply To**: Post 407 (Jayaram, 22f3002723)
- **Content**:  
  Your docker failed to build from your Dockerfile
<pre><code class="lang-auto"> =&gt; ERROR [4/7] RUN uv --version                                                                                                                        0.1s
------
 &gt; [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
  23 |     
  24 |     # Verify uv installation
  25 | &gt;&gt;&gt; RUN uv --version
  26 |     
  27 |     # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127
</code></pre>
Since we cannot build your docker from your Docker manifest file we cannot evaluate it.
- **Reactions**: None
- **Post Number**: 434

