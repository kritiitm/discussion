### Post 32
**Post URL**: /t/mock-roe-1-2-3-4-tds-jan-2025/168449/32
- **ID**: 600375
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-26T14:57:00.650Z
- **Content**:  
  Q2: Download and unzip q-least-unique-subjects-from-csv.zip. It has 2 files:
<ol>
<li><code>students.csv</code> has 2 columns:</li>
<li>studentId: A unique identifier for each student</li>
<li>class: The class (including section) of the student</li>
<li><code>subjects.csv</code> has 2 columns:</li>
<li>studentId: The identifier for each student</li>
<li>subject: The name of the subject they have chosen</li>
</ol>
What are the least number of subjects any class has taken up? List the 3 lowest count of subjects in order.
<pre><code class="lang-auto">!unzip /content/q-least-unique-subjects-from-csv.zip -d /content/extracted_folder
import pandas as pd
df1 = pd.read_csv("/content/extracted_folder/students.csv")
df2 = pd.read_csv("/content/extracted_folder/subjects.csv")
merged_df = pd.merge(df1, df2, on="studentId")
class_subject_counts = merged_df.groupby("class")["subject"].nunique()
lowest_subject_counts = class_subject_counts.nsmallest(3)
print(lowest_subject_counts)
</code></pre>
<span class="mention">@all</span>
- **Reactions**: heart (3)
- **Post Number**: 32

