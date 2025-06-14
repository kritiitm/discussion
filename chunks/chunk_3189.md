### Post 126
**Post URL**: /t/tds-official-project1-discrepencies/171141/126
- **ID**: 613139
- **Author**: Santosh Sharma (Santoshsharma)
- **Created At**: 2025-03-30T05:06:28.932Z
- **Content**:  
  Greetings, Sir,
I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between <code>pandas</code> and <code>numpy</code> caused the container to fail. To my surprise, the same versions (<code>pandas==2.0.3</code> and <code>numpy==1.24.3</code>) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.
To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.
I’ve pushed the updated image to Docker Hub (<code>santoshsharma003/tds-project-one-1:latest</code>). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.
Thank you for your assistance!
- **Reactions**: None
- **Post Number**: 126

