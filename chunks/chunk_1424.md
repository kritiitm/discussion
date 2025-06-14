### Post 203
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/203
- **ID**: 592375
- **Author**: Shambhavi  (24f2003130)
- **Created At**: 2025-02-09T06:13:36.894Z
- **Reply To**: Post 189 (Koustubh Ramakrishnan, koustubhr)
- **Content**:  
  The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.<br>
In your output, there are only two unique issueDate values:<br>
2025-02-08T04:00:00-05:00<br>
2025-02-08T16:01:58-05:00<br>
This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you  need to modify your approach by using the actual forecast day for each day instead.
- **Reactions**: None
- **Post Number**: 203

