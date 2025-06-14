### Post 46
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/46
- **ID**: 582213
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-01-20T05:36:20.460Z
- **Reply To**: Post 43 (Tushar Jalan , 23f2003751)
- **Content**:  
  <a class="mention" href="/u/23f2003751">@23f2003751</a><br>
While I understand why you might choose to use <code>flask</code> due to your familiarity with it,<br>
the <code>http.server</code> library is just very simple to use.
The <strong>only extra line of code</strong> you would need inside your <code>get</code> request if you used the <code>http.server</code> library would be:
<code>self.send_header("Access-Control-Allow-Origin", "*")</code>
Try to rewrite your code using <code>http.server</code>  library so that your debugging for simple tasks like this is easy.
The boilerplate code for a <code>get</code> request using the <code>http.server</code> library was already given in Q6. So you have to do very minimal modifications to it and it works like a charm.
Kind regards
- **Reactions**: heart (1)
- **Post Number**: 46

