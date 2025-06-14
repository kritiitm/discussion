### Post 31
**Post URL**: /t/mock-roe-1-2-3-4-tds-jan-2025/168449/31
- **ID**: 600368
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-26T14:49:06.822Z
- **Content**:  
  Q1: Download and unzip q-count-gold-ticket-sales-from-html.zip. It has a set of HTML files, each with tables of 3 columns: Type, Units, and Price.
What is the total sales of all the items in the “Gold” ticket type? Round to 2 decimal places (e.g. 123.40).
<pre data-code-wrap="colab"><code class="lang-colab">!unzip /content/q-count-gold-ticket-sales-from-html.zip -d /content/extracted_folder
</code></pre>
<pre data-code-wrap="python"><code class="lang-python">import os
import pandas as pd
from bs4 import BeautifulSoup




total_sales = 0
html_folder = "/content/extracted_folder"  # Update if the folder name is different

for file in os.listdir(html_folder):
    if file.endswith(".html"):
        file_path = os.path.join(html_folder, file)

        # Step 3: Read the HTML content and extract tables
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        
        tables = pd.read_html(str(soup))  # Extract all tables

        for table in tables:
            if {"Type", "Units", "Price"}.issubset(table.columns):
                # Step 4: Filter "Gold" ticket type and calculate total sales
                table["Type"] = table["Type"].str.strip().str.lower()
                gold_sales = table[table["Type"] == "gold"]["Units"] * table[table["Type"] == "gold"]["Price"]
                total_sales += gold_sales.sum()
# Step 5: Print the result rounded to 2 decimal places
print(f"Total Gold Ticket Sales: {total_sales:.2f}")

</code></pre>
<span class="mention">@all</span>
- **Reactions**: heart (3)
- **Post Number**: 31

