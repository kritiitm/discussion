### Post 51
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/51
- **ID**: 582645
- **Author**: Mishkat Chougule (23F300327)
- **Created At**: 2025-01-21T08:35:03.754Z
- **Reply To**: Post 50 (Mishkat Chougule, 23F300327)
- **Content**:  
  <pre><code class="lang-auto">from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the CSV file into a DataFrame
data = pd.read_csv('marks.csv')

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from query parameters
    names = request.args.getlist('name')
    
    # Ensure the order of the names in the response matches the query
    marks = [
        int(data[data['name'] == name]['marks'].values[0]) if not data[data['name'] == name].empty else None 
        for name in names
    ]
    
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
</code></pre>
this is the 2nd code I am trying but same error TypeError: Failed to fetch
- **Reactions**: None
- **Post Number**: 51

