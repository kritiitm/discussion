### Post 74
**Post URL**: /t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/74
- **ID**: 584251
- **Author**: Jivraj Singh Shekhawat (Jivraj)
- **Created At**: 2025-01-23T21:26:50.926Z
- **Reply To**: Post 70 (Srividhya, 23ds1000022)
- **Content**:  
  Hi Srividhya,
This error is because you are trying to access a feature of ngrok which requires to pay <a href="https://ngrok.com/docs/errors/err_ngrok_501/#:~:text=Only%20Personal%2C%20Pro%2C%20Enterprise%2C%20or%20Pay-as-you-go%20accounts%20can,resolving%20this%20error%2C%20please%20reach%20out%20to%20support%40ngrok.com" rel="noopener nofollow ugc">ERR_NGROK_501 | ngrok documentation</a>.
I think you didn’t use authtoken to authenticate through your laptop. Follow second step on this page <a href="https://ngrok.com/docs/getting-started/" rel="noopener nofollow ugc">Quickstart | ngrok documentation</a> to authenticate.
kind regards<br>
Jivraj
- **Reactions**: None
- **Post Number**: 74

