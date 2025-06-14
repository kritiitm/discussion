### Post 36
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/36
- **ID**: 587902
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-01-30T12:51:19.538Z
- **Content**:  
  evaluate.py<br>
TDS course repo<aside class="onebox githubfolder" data-onebox-src="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" target="_blank" rel="noopener nofollow ugc">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·...</a></h3>


  <span class="label1">Contribute to sanand0/tools-in-data-science-public development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

line 20
<pre><code class="lang-auto">from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)
</code></pre>
but we get datagen.py only in a1 task<br>
line 69
<pre><code class="lang-auto">async def a1(email: str, **kwargs):
    await run(
        f"""
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`
with `{email}` as the only argument
"""
    )
    return email in await read("/data/format.md")
</code></pre>
The issue is <strong>importing <code>datagen</code> before ensuring it exists</strong>
just checking
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
- **Reactions**: None
- **Post Number**: 36

