### Post 314
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/314
- **ID**: 595074
- **Author**: Jayaram (22f3002723)
- **Created At**: 2025-02-14T16:57:01.976Z
- **Content**:  
  when trying to use function call way of open api
<pre><code class="lang-auto">tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_email_sender",
            "description": "Extract sender email from a specific file in directory",
            "parameters": {},
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_day_of_week",
            "description": "To count the occurances of a specific day of a week in a file with various dates",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_of_week": {
                        "type": "string",
                        "description": "day of week"
                    }
                },
                "required": ["day_of_week"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]
</code></pre>
<pre><code class="lang-auto">    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_input},
                
        ],      
	"tools": tools,
    "tool_choice": "auto",
    "max_tokens": 500,
    "temperature": 0.7
    }
</code></pre>
facing the below issue<br>
ror’: {‘message’: “Invalid type for ‘tools[0]’: expected an object, but got an array instead.”
- **Reactions**: None
- **Post Number**: 314

