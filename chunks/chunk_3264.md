### Post 200
**Post URL**: /t/tds-official-project1-discrepencies/171141/200
- **ID**: 614344
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-04-01T17:35:45.124Z
- **Reply To**: Post 183 (Shreyan Chaubey, thinkmachine)
- **Content**:  
  Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.
<pre><code class="lang-auto">tags = httpx.get(
                f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
            ).json()
            tag, size = next(
                (
                    (tag["name"], tag["full_size"])
                    for tag in tags.get("results", [])
                    if pd.Timestamp(tag["last_updated"]) &lt;= DEADLINE
                ),
                (None, 0),
            )

</code></pre>
This is part of our script that does the validation check for docker repo.
- **Reactions**: heart (1)
- **Post Number**: 200

