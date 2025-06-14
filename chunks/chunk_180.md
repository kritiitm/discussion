### Post 27
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/27
- **ID**: 579910
- **Author**: Mishkat Chougule (23F300327)
- **Created At**: 2025-01-15T07:10:33.142Z
- **Reply To**: Post 25 (Carlton D'Silva, carlton)
- **Content**:  
  <pre><code class="lang-auto">from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the specified CSV file
students = []
with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(class: Optional[List[str]] = Query(None)): 
    """
    Retrieves a list of students, optionally filtered by class.

    Args:
        class: A list of class names to filter by. If None, returns all students.

    Returns:
        A dictionary containing a list of students.
    """
    print(f"Requested classes: {class}")  # Debugging line
    if class:
        filtered_students = [student for student in students if student["class"] in class]
    else:
        filtered_students = students
    print(f"Filtered students: {filtered_students}")  # Debugging line
    return {"students": filtered_students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

</code></pre>
<a class="mention" href="/u/jivraj">@Jivraj</a> this is the code I’m executing which is not getting accepted in the answer box the last time I modified the code it got accepted and I also saved the answer but when I reopened the page till now it is not getting accepted
- **Reactions**: None
- **Post Number**: 27

