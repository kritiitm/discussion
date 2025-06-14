### Post 14
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/14
- **ID**: 579600
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-01-14T10:30:40.928Z
- **Reply To**: Post 13 (Mishkat Chougule, 23F300327)
- **Content**:  
  Hi Mishkat,
This error is because you are filtering on <code>class_</code> instead of <code>class</code>
So if you send a request on <code>http://127.0.0.1/api?class_=1S</code> you will see response for that <code>1S</code> class only.
kind regards
- **Reactions**: None
- **Post Number**: 14

