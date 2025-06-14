### Post 369
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/369
- **ID**: 595273
- **Author**: Saravanan (sarvan108)
- **Created At**: 2025-02-15T08:24:19.337Z
- **Reply To**: Post 4 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  How to resolve this?<br>
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ uv run app.py<br>
Traceback (most recent call last):<br>
File “/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro/app.py”, line 10, in <br>
from fastapi import FastAPI<br>
ModuleNotFoundError: No module named ‘fastapi’<br>
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ pip show fastapi<br>
WARNING: Package(s) not found: fastapi<br>
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ pip install fastapi<br>
error: externally-managed-environment
× This environment is externally managed<br>
╰─&gt; To install Python packages system-wide, try apt install<br>
python3-xyz, where xyz is the package you are trying to<br>
install.
<pre><code>If you wish to install a non-Debian-packaged Python package,
create a virtual environment using python3 -m venv path/to/venv.
Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
sure you have python3-full installed.

If you wish to install a non-Debian packaged Python application,
it may be easiest to use pipx install xyz, which will manage a
virtual environment for you. Make sure you have pipx installed.

See /usr/share/doc/python3.12/README.venv for more information.
</code></pre>
note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.<br>
hint: See PEP 668 for the detailed specification.
- **Reactions**: None
- **Post Number**: 369

