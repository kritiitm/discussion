### Post 45
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/45
- **ID**: 582046
- **Author**: Tushar Jalan  (23f2003751)
- **Created At**: 2025-01-19T13:50:57.854Z
- **Reply To**: Post 44 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  <pre><code class="lang-auto">{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api",
      "dest": "app.py"
    }
  ],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Credentials", "value": "true" },
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET,OPTIONS,PATCH,DELETE,POST,PUT"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
        }
      ]
    }
  ]
}
</code></pre>
<a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a><br>
i have added the header key in order to use the cors as said in the vercel doc but still i am getting that error.<br>
what to do?<br>
i have added the cors in the app.py file as well
<pre><code class="lang-auto">from flask import Flask, request, jsonify
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load the data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)


@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [student["marks"] for student in data if student["name"] in names]
    return jsonify({"marks": marks})


if __name__ == "__main__":
    app.run()

</code></pre>
<a href="https://student-marks-4vsd75x3f-tushars-projects-f2a54030.vercel.app/api" class="onebox" target="_blank" rel="noopener nofollow ugc">https://student-marks-4vsd75x3f-tushars-projects-f2a54030.vercel.app/api</a>
- **Reactions**: None
- **Post Number**: 45

