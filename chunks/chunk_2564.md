### Post 244
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/244
- **ID**: 613840
- **Author**: VIKASH PRASAD (21f3002277)
- **Created At**: 2025-03-31T10:51:38.767Z
- **Content**:  
  what is the problem in my Dockerfile it’s not working and crashing my system
<pre><code class="lang-auto"># Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHON_VERSION=3.11

# Install system dependencies
RUN apt-get update &amp;&amp; apt-get install -y \
    python3.11 \
    python3-pip \
    python3-dev \
    git \
    curl \
    wget \
    ffmpeg \
    imagemagick \
    build-essential \
    libpq-dev \
    &amp;&amp; rm -rf /var/lib/apt/lists/*

# Ensure python3.11 is the default python version
RUN ln -sf /usr/bin/python3.11 /usr/bin/python

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh &amp;&amp; \
    bash nodesource_setup.sh &amp;&amp; \
    apt-get install -y nodejs &amp;&amp; \
    node -v &amp;&amp; \
    npm install -g prettier@3.4.2


# Copy dependencies file first to leverage caching
COPY re.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r re.txt

# Install `uv` package manager from Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create and set working directory
WORKDIR /app

# Copy application files
COPY main.py .
COPY llm_functions.py .
COPY llm_tools_functions_calls.py .
COPY server.py .

# Set default command to start the FastAPI server with `uv`
CMD ["uv", "run", "main.py"]

</code></pre>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
- **Reactions**: None
- **Post Number**: 244

