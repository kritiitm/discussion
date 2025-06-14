### Post 1
**Post URL**: /t/q3-ga5-not-accepting-right-answer/168011/1
- **ID**: 598100
- **Author**: Muskan Aggarwal (muskan2431)
- **Created At**: 2025-02-21T18:32:17.871Z
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/158680f0acc5ef430efd87e8a1cc59a78e6d5e07.png" data-download-href="/uploads/short-url/34qcnwBcLwmxZulqWMVZUZGT9gX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/158680f0acc5ef430efd87e8a1cc59a78e6d5e07.png" alt="image" data-base62-sha1="34qcnwBcLwmxZulqWMVZUZGT9gX" width="690" height="352" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1337×683 31.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It seems that the question in <em>Graded Assignment 5 for TDS</em> is producing incorrect results despite the same logic working correctly for other variations of the problem. Please check into this question once as I have cross checked with many of the students and chatgpt and all of us faced  this issue in this question. Thanks!<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a>
code to take reference from:
<pre><code class="lang-auto">import gzip
import pandas as pd
from datetime import datetime

log_path = 's-anand.net-May-2024.gz'
start_time = datetime.strptime('01:00:00', '%H:%M:%S').time()
end_time = datetime.strptime('15:00:00', '%H:%M:%S').time()
log_data = []

def parse_log(line):
    parts = line.split(' ')
    log_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
    method, url, status = parts[5][1:], parts[6], int(parts[8])
    return log_time, method, url, status

with gzip.open(log_path, 'rt') as file:
    for entry in file:
        log_time, method, url, status = parse_log(entry)
        if method == 'GET' and url.startswith('/blog/') and 200 &lt;= status &lt; 300:
            if log_time.weekday() == 0 and start_time &lt;= log_time.time() &lt; end_time:
                log_data.append(entry)

print(f"Successful GET requests: {len(log_data)}")
</code></pre>
ps: I shared code after the deadline hopefully no issues there! <img src="https://emoji.discourse-cdn.com/google/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20">
- **Reactions**: None
- **Post Number**: 1

