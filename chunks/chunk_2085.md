### Post 81
**Post URL**: /t/mock-roe-1-2-3-4-tds-jan-2025/168449/81
- **ID**: 602061
- **Author**: S Smriti (23f2000599)
- **Created At**: 2025-03-02T06:14:32.775Z
- **Content**:  
  <pre><code class="lang-auto">from shapely.geometry import Polygon, Point
import json

with open("regions.json", "r") as f:
    data = json.load(f)

pickup_locations = [
    (6.488, -78.0287),
    (32.0198, -99.7243),
    (16.7257, -58.7811),
    (1.9307, 45.4928),
    (-34.6289, 133.0359)
]

cities = data["cities"]
regions = data["regions"]

matching_regions = []

for request_point in pickup_locations:
    point = Point(request_point)
    region_num = 1

    for region in regions:
        region_coordinates = [(cities[city][0], cities[city][1]) for city in region]
        region_polygon = Polygon(region_coordinates)

        if region_polygon.contains(point):
            matching_regions.append(str(region_num))
            break  # Stop checking once a match is found
        region_num += 1

print(",".join(matching_regions))
</code></pre>
I have been trying this for the past 1 day and i still cant get the answer for mock roe 2, q5<br>
2 of my coordinates r not giving any value<br>
can someone please help
<a class="mention" href="/u/carlton">@carlton</a>
- **Reactions**: None
- **Post Number**: 81

