### Post 13
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/13
- **ID**: 579593
- **Author**: Mishkat Chougule (23F300327)
- **Created At**: 2025-01-14T10:12:42.463Z
- **Reply To**: Post 11 (Carlton D'Silva, carlton)
- **Content**:  
  <pre data-code-wrap="python"><code class="lang-python">from fastapi import FastAPI, Query
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
async def get_students(class_: Optional[List[str]] = Query(None)):
    print(f"Requested classes: {class_}")  # Debugging line
    if class_:
        filtered_students = [student for student in students if student["class"] in class_]
        print(f"Filtered students: {filtered_students}")  # Debugging line
        return {"students": filtered_students}
    return {"students": students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
</code></pre>
- **Reactions**: open_mouth (1)
- **Post Number**: 13

