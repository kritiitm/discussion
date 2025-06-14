### Post 545
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/545
- **ID**: 595987
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-16T14:06:32.676Z
- **Reply To**: Post 521 (Vishal Baraiya, TheVishal)
- **Content**:  
  Nice bro, if its getting 8 you are sorted, probably get more later. But Prompting seems a little less info<br>
BUT
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>Structured Outputs</th>
<th>JSON Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td>Outputs valid JSON</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Adheres to schema</td>
<td>Yes (see supported schemas)</td>
<td>No</td>
</tr>
<tr>
<td>Compatible models</td>
<td>gpt-4o-mini, gpt-4o-2024-08-06, and later</td>
<td>gpt-3.5-turbo, gpt-4-* and gpt-4o-* models</td>
</tr>
<tr>
<td>Enabling</td>
<td>response_format: { type: json_schema, json_schema: {strict: true, schema: …} }</td>
<td>response_format: { type: json_object }</td>
</tr>
</tbody>
</table>
</div><pre data-code-wrap="python"><code class="lang-python">    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )
</code></pre>
<aside class="onebox githubblob" data-onebox-src="https://github.com/23f2005593/tds/blob/main/app.py#L142">
  <header class="source">

      <a href="https://github.com/23f2005593/tds/blob/main/app.py#L142" target="_blank" rel="noopener nofollow ugc">github.com/23f2005593/tds</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/23f2005593/tds/blob/main/app.py#L142" target="_blank" rel="noopener nofollow ugc">app.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/23f2005593/tds/blob/main/app.py#L142" rel="noopener nofollow ugc"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="132" style="counter-reset: li-counter 131 ;">
          <li>prompt = (</li>
          <li>    f"The Python code generated for the task '{task}' produced the following error when executed:\n"</li>
          <li>    f"{error_message}\n\n"</li>
          <li>    f"Here is the original code:\n{original_code_data['code']}\n\n"</li>
          <li>    "Please provide a corrected version of the code that fixes the error. Return only a JSON object with:\n"</li>
          <li>    "- code: the corrected Python code as a string\n"</li>
          <li>    "- function_name: name of the main function\n"</li>
          <li>    "- required_libraries: list of required pip packages\n\n"</li>
          <li>    "Make sure the code is simple, direct, and error-free this time. And try not to mess it up like before."</li>
          <li>)</li>
          <li class="selected">try:</li>
          <li>    response = client.chat.completions.create(</li>
          <li>        model="gpt-4o-mini",</li>
          <li>        messages=[{"role": "user", "content": prompt}],</li>
          <li>        temperature=0,</li>
          <li>        response_format={"type": "json_object"}</li>
          <li>    )</li>
          <li>except Exception as exc:</li>
          <li>    logger.error("Error connecting to OpenAI API for auto-fix: %s", exc)</li>
          <li>    raise HTTPException(status_code=500, detail="Connection error during auto-fix. Maybe it's time to admit defeat?")</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

you are taking a chance on that format
- **Reactions**: None
- **Post Number**: 545

