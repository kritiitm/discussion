### Post 62
**Post URL**: /t/remote-online-exam-tds-jan-2025/168832/62
- **ID**: 602227
- **Author**: S Smriti (23f2000599)
- **Created At**: 2025-03-02T08:45:25.844Z
- **Content**:  
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b2ceabebead81102cadc823edd2707035627364.png" data-download-href="/uploads/short-url/hzEXHUtuVLO27Dk4qWGd70DkoNm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7b2ceabebead81102cadc823edd2707035627364_2_690x291.png" alt="image" data-base62-sha1="hzEXHUtuVLO27Dk4qWGd70DkoNm" width="690" height="291" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7b2ceabebead81102cadc823edd2707035627364_2_690x291.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7b2ceabebead81102cadc823edd2707035627364_2_1035x436.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7b2ceabebead81102cadc823edd2707035627364_2_1380x582.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1604×678 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<pre><code class="lang-auto">!pip install tabula-py
import tabula
import pandas as pd
from google.colab import files

# Path to the PDF file
pdf_path = pdf_path = list(files.upload().keys())[0]

# Extract tables from the PDF, specifying pages and multiple_tables=True
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

# Initialize an empty list to store all DataFrames
all_dfs = []

# Iterate through each table and add a "Group" column based on the page number
for i, table in enumerate(tables):
    # Add a "Group" column to the table
    table["Group"] = i + 1  # Group 1 for Page 1, Group 2 for Page 2, etc.
    # Append the table to the list
    all_dfs.append(table)

# Combine all DataFrames into a single DataFrame
df = pd.concat(all_dfs, ignore_index=True)

# Rename columns for easier access (if necessary)
df.columns = ["Maths", "Physics", "English", "Economics", "Biology", "Group"]

# Convert marks to numerical data types
df["Maths"] = pd.to_numeric(df["Maths"], errors="coerce")
df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")
df["English"] = pd.to_numeric(df["English"], errors="coerce")
df["Economics"] = pd.to_numeric(df["Economics"], errors="coerce")
df["Biology"] = pd.to_numeric(df["Biology"], errors="coerce")
df["Group"] = pd.to_numeric(df["Group"], errors="coerce")

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Display the first few rows of the combined DataFrame
print(df.head())

# Display the data types of the columns
print(df.dtypes)
filtered_df = df[(df["Biology"] &gt;= 30) &amp; (df["Group"].between(1, 28))]

total_biology_marks = filtered_df["Maths"].sum()
print(total_biology_marks)
</code></pre>
Ignore the variables name, i got my value as 34919<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/c/1cc84aa343d0e7c6509b859b8eabedd390b2cb64.png" data-download-href="/uploads/short-url/46CuuEZv4QNr9XwBxn7mginw5h2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/c/1cc84aa343d0e7c6509b859b8eabedd390b2cb64.png" alt="image" data-base62-sha1="46CuuEZv4QNr9XwBxn7mginw5h2" width="690" height="170" data-dominant-color="FAF8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">905×223 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
i dont understand why its wrong
- **Reactions**: None
- **Post Number**: 62

