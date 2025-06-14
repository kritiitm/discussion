### Post 122
**Post URL**: /t/tds-official-project1-discrepencies/171141/122
- **ID**: 612890
- **Author**: Carlton D'Silva (carlton)
- **Created At**: 2025-03-29T15:20:02.379Z
- **Reply To**: Post 121 (Mishkat Chougule, 23F300327)
- **Content**:  
  When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.
In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.
But we can detect changes made to the docker repo through our image id. I hope that is clear.
We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.
Kind regards
- **Reactions**: +1 (1), heart (1)
- **Post Number**: 122

