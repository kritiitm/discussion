### Post 76
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/76
- **ID**: 591879
- **Author**: Guddu Kumar Mishra  (22f3001315)
- **Created At**: 2025-02-07T19:50:53.195Z
- **Content**:  
  <pre data-code-wrap="result"><code class="lang-result">    expected = sum(1 for date in dates if parse(date).weekday() == 2)
    if result.strip() != str(expected):
        return mismatch("/data/dates-wednesdays.txt", expected, result)
    return True```


</code></pre>
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> /data/dates-wednesdays.txt<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
129<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
“129”
If it is expecting str then why throw error sir  ? <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a><br>
or just tell me how to pass count as an int here
<pre><code class="lang-auto">with open(output_file, "w") as f:
        f.write(str(count)) 
</code></pre>
- **Reactions**: heart (1)
- **Post Number**: 76

