### Post 149
**Post URL**: /t/tds-official-project1-discrepencies/171141/149
- **ID**: 614015
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-03-31T21:01:54.794Z
- **Reply To**: Post 145 (Abhinav, AbhinavOhri)
- **Content**:  
  The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.
But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.
Kind regards
- **Reactions**: None
- **Post Number**: 149

