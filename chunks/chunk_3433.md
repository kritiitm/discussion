### Post 369
**Post URL**: /t/tds-official-project1-discrepencies/171141/369
- **ID**: 616318
- **Author**: D HARICHARAN  (Haricharan)
- **Created At**: 2025-04-06T19:06:07.077Z
- **Reply To**: Post 358 (Carlton D'Silva, carlton)
- **Content**:  
  Sir actually my project doesn’t have requirements.txt, instead it installs automatically<br>
when:<br>
<code>uv run app.py</code> is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).<br>
my dockerfile from the repo:
<pre><code class="lang-auto">FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh &amp;&amp; rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
</code></pre>
here u can see it installs using pip install …
here it’s requiring <code>.env</code> file to be present in the project folder because my project when I was uploading to both git and docker had <code>.env</code> file for AIPROXY_TOKEN and I uploaded to docker with that <code>.env</code> file but as git doesn’t allow upload of <code>.env</code> file I couldn’t upload<code>.env</code> to git
the project will still work after downloading the repository when we upload AIPROXY_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because<code>.env</code> file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the <code>.env</code> file so it didn’t build so I had to create the <code>.env</code> file now to create the docker image, and for the dockerimage I had submitted, I built it with the <code>.env</code> file(it supports both<code>.env</code> file and environment variable one)
- **Reactions**: None
- **Post Number**: 369

