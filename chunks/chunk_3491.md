### Post 427
**Post URL**: /t/tds-official-project1-discrepencies/171141/427
- **ID**: 616718
- **Author**: Mishkat Chougule (23F300327)
- **Created At**: 2025-04-07T16:23:03.736Z
- **Reply To**: Post 425 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  My code uses <code>npx</code> to format Markdown files using Prettier, specifically via <code>subprocess.run(["npx", "prettier@3.4.2", "--write", ...])</code>, which assumes that <code>npx</code> is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or <code>npx</code>, this results in an error during evaluation.
To test the functionality correctly, <code>npx</code> must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:
bash:<code> apt-get update &amp;&amp; apt-get install -y nodejs npm</code>
Once installed, <code>npx prettier@3.4.2</code> should work as expected.
For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where <code>npx</code> is available by default.
- **Reactions**: None
- **Post Number**: 427

