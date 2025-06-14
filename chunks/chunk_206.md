### Post 52
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/52
- **ID**: 582661
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-01-21T09:02:30.157Z
- **Reply To**: Post 50 (Mishkat Chougule, 23F300327)
- **Content**:  
  <a class="mention" href="/u/23f300327">@23F300327</a>
Typically for a vercel application, and in particular for GA2-Q6, the applications are basically function calls. You are not expected to setup and run a local http server as you are doing in your code.
When a call is made to the endpoint which in this scenario is /api<br>
with parameters, only one function is required, i.e the function that handles the get request.
The rest is also automagically handled by vercel. There might be a conflict between vercel’s webserver deployment and the one you explicitly have encoded in your program.
That’s why if you see in the course content about vercel, the simplest API service that you can launch with vercel looks something like this
<pre><code class="lang-auto"># api/index.py
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return
</code></pre>
Notice there is no <code>if __name__ == "__main__":</code> code block.<br>
This would instruct the interpreter that this is the starting point of your module. Clearly we do not want that, we want vercel to handle all the backend server stuff because vercel might be running some preflight code before it runs your application.
<code>if __name__ == "__main__":</code> is used to execute some code <strong>only</strong> if the file was run directly, and not imported. In vercel, it might not be the starting point of the application.
Try rewriting it with just the required endpoint function inside the default <code>handler</code> class. Avoid custom named classes until you can get a working prototype working using the boilerplate that has been shared.
Another possible problem:<br>
By default, the JSON module encodes Unicode objects (such as str and Unicode) into the \u escape sequence when generating JSON data. The GA however is expecting a serialised  UTF-8 JSON response instead. These might look the same on the screen but are not equivalent at the bytecode level. These encoding problems were covered in one of the videos that talked about encoding issues <a href="https://tds.s-anand.net/#/unicode" rel="noopener nofollow ugc">TDS &gt; Development Tools &gt; unicode</a>
So converting your output to UTF-8 might fix it.
Let us know what worked. We are all learning from each other.
Kind regards
- **Reactions**: None
- **Post Number**: 52

