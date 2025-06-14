### Post 344
**Post URL**: /t/tds-official-project1-discrepencies/171141/344
- **ID**: 616146
- **Author**: Afsal (afsalshah)
- **Created At**: 2025-04-06T14:44:59.635Z
- **Reply To**: Post 191 (Jivraj Singh Shekhawat, Jivraj)
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Dear Sir,<br>
I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.<br>
I debugged that I had a small issue in the dockerfile that was submitted and it is<br>
CMD [“/root/.local/bin/uv”, “run”, “app.py”]  has an <strong>invisible Unicode non-breaking space</strong> (<code>U+00A0</code>) between <code>"run", "app.py"</code> instead of a regular space. This causes the shell to misread the command.<br>
I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE.  Expecting a positive response from your end.
- **Reactions**: None
- **Post Number**: 344

