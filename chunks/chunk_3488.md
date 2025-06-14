### Post 424
**Post URL**: /t/tds-official-project1-discrepencies/171141/424
- **ID**: 616683
- **Author**: Mishkat Chougule (23F300327)
- **Created At**: 2025-04-07T10:31:33.573Z
- **Content**:  
  <pre><code class="lang-auto">🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
  "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1     | 2   |   3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")

</code></pre>
<h1><a name="p-616683-result-header-1" class="anchor" href="#p-616683-result-header-1"></a><img src="https://emoji.discourse-cdn.com/google/warning.png?v=14" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
Header</h1>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:left">Start</th>
<th>Mid</th>
<th style="text-align:right">End</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">1</td>
<td>2</td>
<td style="text-align:right">3</td>
</tr>
</tbody>
</table>
</div>Paragraph has extra   spaces and trailing whitespace.
<pre data-code-wrap="py"><code class="lang-py">print("23f3003027@ds.study.iitm.ac.in")

</code></pre>
<img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> A2 FAILED
<pre><code class="lang-auto">I am facing Npx error... can I know what went wrong?
@carlton @Jivraj</code></pre>
- **Reactions**: None
- **Post Number**: 424

