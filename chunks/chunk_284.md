### Post 131
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/131
- **ID**: 588408
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-02-01T02:50:49.374Z
- **Reply To**: Post 129 (Srividhya, 23ds1000022)
- **Content**:  
  Hi Srividya,
Thats right the idea behind vercel is you do not need to create a server. Its serverless! Instead you create functions that respond to endpoints.<br>
When the endpoint is triggered, the appropriate function runs.
This renders <code>name == main</code> part of the code unnecessary at best, since python interpreters only run this line if that file was the starting point of the application (but its not, because a vercel wrapper application(s) or processes have started before it).
In other words you do not create a flask server, or a http server or indeed any server at all. Just functions tied to specific endpoints. So you have to rethink how your application is designed. You <em>do not</em> create serverless applications in the same traditional way you have been taught in MAD-1 or MAD-2.
This is a common mistake many students have been making with their approach to vercel. Watching the videos and using the provided code template will greatly help in deploying successful serverless applications.
Thanks for your input.
Kind regards
- **Reactions**: heart (1)
- **Post Number**: 131

