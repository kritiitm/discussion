### Post 64
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/64
- **ID**: 591135
- **Author**: Anand S (s.anand)
- **Created At**: 2025-02-06T07:29:30.529Z
- **Reply To**: Post 63 (Hriday Pradhan, 21f3002390)
- **Content**:  
  <a class="mention" href="/u/21f3002390">@21f3002390</a> - AI Proxy is working and you <em>did</em> get the result. You can ignore any <code>costError</code>. It won’t happen in the future anyway.
<strong>What’s happening?</strong> I was trying to generate a unique hash for each request, as a precursor to caching requests. But I made a mistake in the code. Specifically, <code>crypto.createHash</code> is not supported in CloudFlare. <a href="https://github.com/sanand0/aiproxy/commit/5943b6d355deffff88ac07d17aa0c6969cacc3d5">I fixed that</a> by removing this. I’ll introduce caching later if required.
- **Reactions**: heart (2), +1 (1)
- **Post Number**: 64

