### Post 99
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/99
- **ID**: 611169
- **Author**: Tushar Jalan  (23f2003751)
- **Created At**: 2025-03-24T15:44:47.263Z
- **Content**:  
  <pre><code class="lang-auto">// GA1 question 9:
    //     curl -X POST "http://localhost:8000/api/" -H "Content-Type: multipart/form-data" -F "question=Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines. 
    // [{\"name\":\"Alice\",\"age\":92},{\"name\":\"Bob\",\"age\":28},{\"name\":\"Charlie\",\"age\":16},{\"name\":\"David\",\"age\":56},{\"name\":\"Emma\",\"age\":70},{\"name\":\"Frank\",\"age\":67},{\"name\":\"Grace\",\"age\":36},{\"name\":\"Henry\",\"age\":94},{\"name\":\"Ivy\",\"age\":44},{\"name\":\"Jack\",\"age\":53},{\"name\":\"Karen\",\"age\":65},{\"name\":\"Liam\",\"age\":23},{\"name\":\"Mary\",\"age\":97},{\"name\":\"Nora\",\"age\":68},{\"name\":\"Oscar\",\"age\":57},{\"name\":\"Paul\",\"age\":88}]"
    {
        "answer": "[{\"name\":\"Charlie\",\"age\":16},{\"name\":\"Liam\",\"age\":23},{\"name\":\"Bob\",\"age\":28},{\"name\":\"Grace\",\"age\":36},{\"name\":\"Ivy\",\"age\":44},{\"name\":\"Jack\",\"age\":53},{\"name\":\"David\",\"age\":56},{\"name\":\"Oscar\",\"age\":57},{\"name\":\"Karen\",\"age\":65},{\"name\":\"Frank\",\"age\":67},{\"name\":\"Nora\",\"age\":68},{\"name\":\"Emma\",\"age\":70},{\"name\":\"Paul\",\"age\":88},{\"name\":\"Alice\",\"age\":92},{\"name\":\"Henry\",\"age\":94},{\"name\":\"Mary\",\"age\":97}]"
    }
</code></pre>
Is it ok for GA 1 Question 9 answer output to look like this because it matches with the answer just it has the extra back slash…What should i do
<pre><code class="lang-auto">def sort_json_array(json_array: str, sort_keys: list) -&gt; str:
    """
    Sort a JSON array based on specified criteria

    Args:
        json_array: JSON array as a string
        sort_keys: List of keys to sort by

    Returns:
        Sorted JSON array as a string
    """
    try:
        # Parse the JSON array
        data = json.loads(json_array)

        # Sort the data based on the specified keys
        for key in reversed(sort_keys):
            data = sorted(data, key=lambda x: x.get(key, ""))

        # Return the sorted JSON as a string without whitespace
        return json.dumps(data, separators=(",", ":"))

    except Exception as e:
        return f"Error sorting JSON array: {str(e)}"
</code></pre>
<pre><code class="lang-auto">{
            "type": "function",
            "function": {
                "name": "sort_json_array",
                "description": "Sort a JSON array based on specified criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "json_array": {
                            "type": "string",
                            "description": "JSON array to sort",
                        },
                        "sort_keys": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of keys to sort by",
                        },
                    },
                    "required": ["json_array", "sort_keys"],
                },
            },
        },
</code></pre>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/e/2e577720e007a687c9e3aeecd301efb7b64eb222.gif" alt="sad me" data-base62-sha1="6BXm9nyXzURxtfunKKGafzV2nbY" width="110" height="110" class="animated">
- **Reactions**: heart (1)
- **Post Number**: 99

