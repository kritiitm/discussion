### Post 50
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/50
- **ID**: 582633
- **Author**: Mishkat Chougule (23F300327)
- **Created At**: 2025-01-21T08:09:40.078Z
- **Reply To**: Post 48 (Carlton D'Silva, carlton)
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/5/9540d770e250d10f3b19c38ce563192219676d6e.png" data-download-href="/uploads/short-url/lim43PiXEjdjlXTI4ijfw7jeqDQ.png?dl=1" title="Screenshot 2025-01-21 at 1.37.06 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/9540d770e250d10f3b19c38ce563192219676d6e_2_690x431.png" alt="Screenshot 2025-01-21 at 1.37.06 PM" data-base62-sha1="lim43PiXEjdjlXTI4ijfw7jeqDQ" width="690" height="431" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/9540d770e250d10f3b19c38ce563192219676d6e_2_690x431.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/9540d770e250d10f3b19c38ce563192219676d6e_2_1035x646.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/9540d770e250d10f3b19c38ce563192219676d6e_2_1380x862.png 2x" data-dominant-color="0D0B0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-21 at 1.37.06 PM</span><span class="informations">1440×900 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
when I paste the url it is showing TypeError: Failed to fetch<br>
my code:
<pre><code class="lang-auto">import json
import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Load the CSV file into a DataFrame
try:
    data = pd.read_csv('marks.csv')
except FileNotFoundError:
    data = None

class MarksHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if data is None:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "marks.csv not found"}).encode())
            return

        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        names = query_params.get('name', [])  # Get list of names from query parameters

        marks = [
            int(data[data['name'] == name]['marks'].values[0]) if not data[data['name'] == name].empty else None 
            for name in names
        ]

        response = json.dumps({"marks": marks})
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()
        self.wfile.write(response.encode())

if __name__ == "__main__":
    server_address = ('', 8000)  # Run on port 8000
    httpd = HTTPServer(server_address, MarksHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()
</code></pre>
- **Reactions**: None
- **Post Number**: 50

