### Post 123
**Post URL**: /t/project-2-tds-solver-discussion-thread/169029/123
- **ID**: 611821
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-03-27T07:05:51.741Z
- **Reply To**: Post 122 (Shivaditya Bhattacharya, 22f3000819)
- **Content**:  
  Your markdown must have newline characters or spaces wherever necessary. Otherwise we will not be able to check if your answer is correct. Our parser will only work if encodings for the formatting are present in the response. If there are no encodings (invisible or visible) then we will not have the correctly formatted file.
Please review module 1 for a better understanding about how text is encoded. Especially invisible characters.
The browser is designed for user friendliness. Thats why the characters are invisible when you copy paste string with newlines. But it exists.
The programmatic strings show invisible encodings as escaped characters. (Usually)
To check if a string has invisible characters,
<pre><code class="lang-auto"># Multi-line string
my_string = """Hello
World    with    spaces 
and some newlines
and a tab	"""

# Print ASCII values of each character
print([ord(c) for c in my_string])
</code></pre>
e.g., newline = 10, tab = 9
This is a great way to check what we are receiving when you send us some response,
<pre><code class="lang-auto">import requests
import json

# This is just an example server to see what we see.

url = "https://httpbin.org/post"

my_multiline_string_answer = """This is a multiline
string that spans
multiple lines    with    spaces 
and some newlines
and a tab	as well."""

response_to_send_to_tds_evaluator = {
"answer": my_multiline_string_answer
}

# Send the JSON data
response = requests.post (url, json=response_to_send_to_tds_evaluator)

# Check the response
print (response.status_code)
print (response.json ())
print (response.text)

# Do other checks as necessary... 
</code></pre>
See what happens when I print the result
<pre><code class="lang-auto">print (json.loads (response.text)['json']['answer'])
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad116ba310657f4688bc4744ea6f291fddcb63b8.png" data-download-href="/uploads/short-url/oH1VnNagrJMWv1kL9vEZ36eOUoU.png?dl=1" title="Screenshot 2025-03-27 at 1.09.56 pm"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad116ba310657f4688bc4744ea6f291fddcb63b8.png" alt="Screenshot 2025-03-27 at 1.09.56 pm" data-base62-sha1="oH1VnNagrJMWv1kL9vEZ36eOUoU" width="323" height="120"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-27 at 1.09.56 pm</span><span class="informations">323×120 3.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Its a proper multiline correctly formatted text! The encodings are invisible just like in the original as well as in your clipboard when you copy paste into the GA.
Here is a json example:
<pre><code class="lang-auto">json_answer = {
    "mary": "poppins",
    "age": 42
}

stringed_json = json.dumps (json_answer)
response_to_send_to_tds_evaluator = {
"answer": stringed_json
}

response = requests.post (url, json=response_to_send_to_tds_evaluator)

print (json.loads (response.text)['json']['answer'])
</code></pre>
Look at the response. A perfect json.<br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/df98b9abfbf5f7d32de578c727f25b166a564560.png" alt="Screenshot 2025-03-27 at 3.30.17 pm" data-base62-sha1="vU1GFSDk4aLLFTjZzOv1PffvXl6" width="287" height="59">
If you do not want spaces in the response then strip the spaces before you send the stringified response.
Kind regards
- **Reactions**: None
- **Post Number**: 123

