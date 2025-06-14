### Post 87
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/87
- **ID**: 609652
- **Author**: Shivaditya Bhattacharya (22f3000819)
- **Created At**: 2025-03-22T07:20:54.446Z
- **Reply To**: Post 85 (Shashannk, 23f2003413)
- **Content**:  
  Use the following script to enable answer boxes and check answers buttons:
<pre><code class="lang-auto">inputs = document.querySelectorAll('input')
textboxes = document.querySelectorAll("textarea")
buttons  = document.querySelectorAll("button")
inputs.forEach(input =&gt; input.removeAttribute('disabled'));
buttons.forEach(input =&gt; input.removeAttribute('disabled'));
textboxes.forEach(input =&gt; input.removeAttribute('disabled'));
</code></pre>
This was provided with the Mock ROE2 mail.
- **Reactions**: heart (3)
- **Post Number**: 87

