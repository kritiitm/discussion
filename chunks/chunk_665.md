### Post 138
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/138
- **ID**: 594022
- **Author**: Adithya S (Adithya)
- **Created At**: 2025-02-12T06:27:17.724Z
- **Content**:  
  <em>For task A2</em>:
<ul>
<li><strong>A2</strong>. Format the contents of <code>/data/format.md</code> using <code>prettier@3.4.2</code>, updating the file in-place</li>
</ul>
I am getting the following error:<br>
<code>🔴 A2 failed: Command '['npx', 'prettier@3.4.2', '--stdin-filepath', '/data/format.md']' returned non-zero exit status 1.</code>
However, running a <strong>POST request</strong> to <a href="https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2" rel="noopener nofollow ugc">https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2</a> gives successful output.
<code>{"success":true,"message":"Formatted and verified successfully!"}% </code>
Here is my code snippet:
<pre data-code-wrap="py"><code class="lang-py">def format_file(filepath):
    while True:  # Loop until formatting and verification pass
        try:
            result = subprocess.run(
                ["npx", "prettier@3.4.2", "--write", filepath],
                check=False,  # Don't raise exception automatically
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return {"success": False, "message": f"Prettier write failed: {result.stderr}"}

            if verify_prettier_formatting(filepath):
                return {"success": True, "message": "Formatted and verified successfully!"}
            else:
                logging.info("Verification failed. Retrying formatting...") #Log the retry
                # If verification fails, the loop continues and prettier --write is executed again.

        except Exception as e:
            return {"success": False, "message": str(e)}

def verify_prettier_formatting(filepath):
    try:
        subprocess.run(["npx", "prettier@3.4.2", "--check", filepath], check=True, capture_output=True, text=True) #Capture output
        return True  # File is formatted correctly
    except subprocess.CalledProcessError as e:
        logging.error(f"Prettier check failed: {e.stderr}") # Log the error from prettier check
        return False  # File is not formatted correctly
</code></pre>
What am I missing here?
- **Reactions**: +1 (1)
- **Post Number**: 138

