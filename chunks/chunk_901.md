### Post 374
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/374
- **ID**: 595295
- **Author**: JAIDEEP M (Jaideep)
- **Created At**: 2025-02-15T08:59:45.643Z
- **Reply To**: Post 369 (Saravanan, sarvan108)
- **Content**:  
  it usually happens in some GNU/Linux OS. since you are using some distribution based on Debian namely Ubuntu or whatever try doing sudo apt install python-packagename (replace package name with fastapi for fastapi)<br>
then it works. It usually happens due to manual intervention with pip3 the user might break some system dependencies which require some python3 package. No need to worry about it.<br>
Another Fix: try using a virtual environment which is highly suggested since there is no chance for you to interfere with the system packages.<br>
create a venv using python3 -m venv name_of_venv<br>
add this line to your .bashrc in ~ folder as source /path/to/your/venv/location<br>
and run source .bashrc. This time no error occurs as you do everything in your virtual environment you can install anything python3 package using pip3 install package name.<br>
It even happened for me
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac.png" data-download-href="/uploads/short-url/37CTgqCCMcH8aqhG6ZxcO9HICyE.png?dl=1" title="Screenshot_20250215_143357" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_690x181.png" alt="Screenshot_20250215_143357" data-base62-sha1="37CTgqCCMcH8aqhG6ZxcO9HICyE" width="690" height="181" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_690x181.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_1035x271.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_1380x362.png 2x" data-dominant-color="282B2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20250215_143357</span><span class="informations">3841×1009 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
- **Reactions**: None
- **Post Number**: 374

