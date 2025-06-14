### Post 1
**Post URL**: /t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/1
- **ID**: 594941
- **Author**: SAKSHI PATHAK (Sakshi6479)
- **Created At**: 2025-02-14T12:38:47.883Z
- **Content**:  
  sir i am getting an error in this function calling which you have demonstrate yesterday , i am attaching my code also the error with it. Please take a look and provide the solution as the deadline is close please help me as soon as possible.<br>
is there anything to do with dockerfile or anything else please explain it how to do it step by step.
<pre><code class="lang-auto">import os
from dotenv import load_dotenv
import json
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
load_dotenv()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "enter your token here")


def sort_contacts(contacts_file_path: str, output_file_path: str):
    try:
        contacts = pd.read_json(contacts_file_path)
        contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
        return {"message": f"Contacts sorted and saved to {output_file_path}"}
    except Exception as e:
        return {"error": f"Failed to sort contacts: {str(e)}"}


a4_tool = {
    "type": "function",
    "function": {
        "name": "sort_contacts",
        "description": "This function takes data from a json file and sorts the data first by last name and then by first name, then it stores it inside the speicfied location.",
        "parameters": {
            "type": "object",
            "properties": {
                "contacts_file_path": {
                    "type": "string",
                    "description": "The relative path to the input JSON file containing the contacts."
                },
                "output_file_path": {
                    "type": "string",
                    "description": "The relative path to the output JSON file to store the sorted contacts."
                }
            },
            "required": ["contacts_file_path", "output_file_path"],
            "additionalProperties": False
        },
        "strict": True
    },
}


tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]



def query_gpt(user_input: str, tools: list[dict] = tools) -&gt; dict:
    response = requests.post(
        url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AIPROXY_TOKEN}"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "tools": tools,
            "tool_choice": "auto"
        }
    )
    return response.json()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail="File does not exist")

@app.post("/run")
async def run(task: str):
    query = query_gpt(task)
    print(query)  # Print the full response to inspect it.
    
    if 'choices' not in query:
        raise HTTPException(status_code=500, detail="Invalid response format from GPT API")
    
    try:
        tool_calls = query['choices'][0]['message'].get('tool_calls', [])
        if tool_calls:
            func_name = tool_calls[0]['function']['name']
            args = json.loads(tool_calls[0]['function']['arguments'])
            
            # Map function names to their respective functions
            function_map = {
                "cakebake": cakebake,
                "install_uv_and_run_datagen": install_uv_and_run_datagen,
                "format_markdown_file": format_markdown_file,
                "count_wednesdays": count_wednesdays,
                "sort_contacts": sort_contacts,
                "extract_recent_logs": extract_recent_logs,
                "create_markdown_index": create_markdown_index,
                "extract_sender_email": extract_sender_email,
                "extract_credit_card_number": extract_credit_card_number,
                "find_similar_comments": find_similar_comments,
                "calculate_gold_ticket_sales": calculate_gold_ticket_sales,
            }
            
            if func_name in function_map:
                output = function_map[func_name](**args)
            else:
                raise HTTPException(status_code=500, detail="Unknown function called")
        else:
            raise HTTPException(status_code=500, detail="No function call found in response")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
    
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/255972d284f089960091b482f45a9c8f83919195.png" data-download-href="/uploads/short-url/5kpj9Kh1zIaAJZmIig1SCQTXOtL.png?dl=1" title="Screenshot 2025-02-14 171217" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/255972d284f089960091b482f45a9c8f83919195_2_690x446.png" alt="Screenshot 2025-02-14 171217" data-base62-sha1="5kpj9Kh1zIaAJZmIig1SCQTXOtL" width="690" height="446" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/255972d284f089960091b482f45a9c8f83919195_2_690x446.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/255972d284f089960091b482f45a9c8f83919195_2_1035x669.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/255972d284f089960091b482f45a9c8f83919195_2_1380x892.png 2x" data-dominant-color="272728"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-14 171217</span><span class="informations">2075×1343 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> , <a class="mention" href="/u/carlton">@carlton</a>
- **Reactions**: None
- **Post Number**: 1

