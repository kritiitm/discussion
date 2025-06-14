### Post 66
**Post URL**: /t/tds-official-project1-discrepencies/171141/66
- **ID**: 612500
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-03-29T07:15:09.835Z
- **Reply To**: Post 64 (Ritwika Dutta , 22f2001389)
- **Content**:  
  Yeah, it’s there on your local machine, but you didn’t copy it to docker container.<br>
Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.
<pre><code class="lang-auto">FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh &amp;&amp; rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
</code></pre>
- **Reactions**: None
- **Post Number**: 66

