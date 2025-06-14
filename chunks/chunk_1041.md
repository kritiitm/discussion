### Post 514
**Post URL**: /t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/514
- **ID**: 595847
- **Author**: Ayush Kumar Shaw  (23f2001286)
- **Created At**: 2025-02-16T09:19:36.290Z
- **Content**:  
  More Particularily the failure occurs in the response portion…
<pre><code class="lang-auto">def get_completions(prompt: str):
    print("Inside get_completions")#Debug
    with httpx.Client(timeout=20) as client:
        response = client.post(
            f"{openai_api_chat}",
            headers=headers,
            json=
                {
                    "model": "gpt-4o-mini",
                    "messages": [
                                    {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
                                    {"role": "user", "content": prompt}
                                ],
                    "tools": [
                                {
                                    "type": "function",
                                    "function": function
                                } for function in function_definitions_llm
                            ],
                    "tool_choice": "auto"
                },
        )

    print("DId suceessful llm calll")#Debug
</code></pre>
<pre><code class="lang-auto">INFO:     127.0.0.1:52108 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 400 Bad Request
</code></pre>
- **Reactions**: None
- **Post Number**: 514

