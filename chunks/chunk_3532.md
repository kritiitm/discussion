### Post 468
**Post URL**: /t/tds-official-project1-discrepencies/171141/468
- **ID**: 618525
- **Author**: Hilal (22f2000526)
- **Created At**: 2025-04-12T07:38:59.014Z
- **Reply To**: Post 454 (Carlton D'Silva, carlton)
- **Content**:  
  <a class="mention" href="/u/carlton">@carlton</a><br>
Thank you i found my mistake in my docker file i wrote  this  CMD [“uv”, “run”, “app.py”]  instead of<br>
CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine
- **Reactions**: None
- **Post Number**: 468

