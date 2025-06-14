### Post 139
**Post URL**: /t/tds-official-project1-discrepencies/171141/139
- **ID**: 613878
- **Author**: Shiva Ramakrishna (Mystic_9803)
- **Created At**: 2025-03-31T12:59:59.522Z
- **Content**:  
  Hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe_open function that will throw a HTTP_403_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?
Thanks for considering, any help would be appreciated. Worked very hard for this
- **Reactions**: None
- **Post Number**: 139

