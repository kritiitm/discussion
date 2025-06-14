### Post 316
**Post URL**: /t/tds-official-project1-discrepencies/171141/316
- **ID**: 616053
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-04-06T12:22:00.340Z
- **Reply To**: Post 302 (HariOm Pandey, 21f3002112)
- **Content**:  
  To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.
<pre data-code-wrap="python"><code class="lang-python"># /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
    "--owner",
    type=str,
    required=True,
    help="GitHub username."
)
parser.add_argument (
    "--repo",
    type=str,
    required=True,
    help="GitHub repository name."
)
parser.add_argument (
    "--save",
    type=str,
    default="../github/",
    help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
    "--extract",
    type=str,
    default="../github/",
    help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&amp;per_page=1&amp;page=1"

try:
    response = requests.get (url, headers=github_headers, timeout=60)
    response.raise_for_status ()  # Raise an error for bad responses

    # Get the sha
    commits = response.json ()
    if commits:
        latest_sha = commits[0]["sha"]
        print (f"Latest commit before {deadline_str}: {latest_sha}")

        # Get the zip of the commit
        zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
        zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
        zip_response.raise_for_status ()
        zip_filename = f"{latest_sha}.zip"

        # Create the directory if it doesn't exist
        os.makedirs (save_path, exist_ok=True)

        with open (save_path + zip_filename, "wb") as f:
            f.write (zip_response.content)
        print (f"Downloaded zip file: {zip_filename}")

        # Create the directory if it doesn't exist
        os.makedirs (extract_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
            zip_ref.extractall (extract_path)
        print (f"Extracted zip file to: {extract_path}")

    else:
        print (f"No commits found before {deadline_str}")

except:
    print(f"Error fetching commits: {response.status_code} - {response.text}")
</code></pre>
Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.
<code>docker build -t &lt;your image name&gt;   .</code>
Run new docker image using<br>
<code>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 &lt;your image name&gt;</code>
Keep datagen.py and evaluate.py in same folder<br>
<code>uv run evaluate.py --email &lt;any email&gt; --token_counter 1 --external_port 8000</code>
This then re-produces the exact environment how your application was  tested.<br>
You have to provide a token from your environment for testing.
These instructions are same for everyone. So check first before posting here.
- **Reactions**: None
- **Post Number**: 316

