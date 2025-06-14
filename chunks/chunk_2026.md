### Post 35
**Post URL**: /t/mock-roe-1-2-3-4-tds-jan-2025/168449/35
- **ID**: 600380
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-02-26T15:18:23.855Z
- **Content**:  
  <span class="mention">@all</span><br>
Q: You are the operations manager for World Courier. You are trying to find the shortest path between <code>Doha</code> and <code>Muscat</code>.
World Courier has a fleet of aircraft that can fly directly between specific cities. The distance between two cities is the <a href="https://pypi.org/project/haversine/" rel="noopener nofollow ugc">Haversine distance</a>.
What is the sequence of cities that you should fly to minimize the total distance traveled?
Write the answer as a sequence of cities separated by commas.
<pre><code class="lang-auto">HTML2= """"
&lt;table class="table"&gt;
        &lt;thead&gt;
          &lt;tr&gt;
            &lt;th&gt;City&lt;/th&gt;
            &lt;th&gt;Latitude&lt;/th&gt;
            &lt;th&gt;Longitude&lt;/th&gt;
          &lt;/tr&gt;
        &lt;/thead&gt;
        &lt;tbody&gt;
          &lt;!--?lit$901276210$--&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;New York&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;40.7128&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;-74.006&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lGET DATA FROM QUESTION
              &lt;/tr&gt;&lt;!----&gt;
        &lt;/tbody&gt;
      &lt;/table&gt;
"""
HTML = """&lt;table class="table"&gt;
        &lt;thead&gt;
          &lt;tr&gt;
            &lt;th&gt;From&lt;/th&gt;
            &lt;th&gt;To&lt;/th&gt;
          &lt;/tr&gt;
        &lt;/thead&gt;
        &lt;tbody&gt;
          &lt;!--?lit$901276210$--&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;New York&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;London&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Tokyo&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Sydney&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Paris&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Berlin&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Dubai&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Mumbai&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;San Francisco&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Tokyo&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Toronto&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;New York&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;&lt;!----&gt;&lt;tr&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Shanghai&lt;/td&gt;
                &lt;td&gt;&lt;!--?lit$901276210$--&gt;Singapore&lt;/td&gt;
              &lt;/tr&gt;&lt;!----&gt;...............GET DATA FROM QUESTION
              &lt;/tr&gt;&lt;!----&gt;
        &lt;/tbody&gt;
      &lt;/table&gt;"""
import pandas as pd
from bs4 import BeautifulSoup
soup = BeautifulSoup(HTML, "html.parser")

# Extract table rows
rows = []
for tr in soup.find_all("tr"):
    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
    if cells:  # Ensure the row is not empty
        rows.append(cells)

# Convert extracted data into a pandas DataFrame
df = pd.DataFrame(rows, columns=["From", "To"])


soup = BeautifulSoup(HTML2, "html.parser")
rows = []
for tr in soup.find_all("tr"):
    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
    if cells:  # Ensure the row is not empty
        rows.append(cells)

# Convert extracted data into a pandas DataFrame
df2 = pd.DataFrame(rows, columns=["City", "Latitude","Longitude"])
import networkx as nx
from math import radians, sin, cos, sqrt, atan2


cities_df = df2


flights_df = df
cities_df["Latitude"] = pd.to_numeric(cities_df["Latitude"])
cities_df["Longitude"] = pd.to_numeric(cities_df["Longitude"])

# Step 3: Define Haversine Distance Function
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))

# Step 4: Build Graph with NetworkX
G = nx.Graph()

for _, row in flights_df.iterrows():
    city1, city2 = row["From"], row["To"]
    
    lat1, lon1 = cities_df[cities_df["City"] == city1][["Latitude", "Longitude"]].values[0]
    lat2, lon2 = cities_df[cities_df["City"] == city2][["Latitude", "Longitude"]].values[0]
    
    distance = haversine(lat1, lon1, lat2, lon2)
    G.add_edge(city1, city2, weight=distance)

# Step 5: Find Shortest Path using Dijkstra's Algorithm
shortest_path = nx.shortest_path(G, source="Doha", target="Muscat", weight="weight")
shortest_distance = nx.shortest_path_length(G, source="Doha", target="Muscat", weight="weight")

# Output the result
print("Shortest Path:", " → ".join(shortest_path))
print(f"Total Distance: {shortest_distance:.2f} km")

</code></pre>
<span class="mention">@all</span>
- **Reactions**: heart (1)
- **Post Number**: 35

