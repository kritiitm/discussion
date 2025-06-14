### Post 31
**Post URL**: /t/tds-official-project1-discrepencies/171141/31
- **ID**: 612365
- **Author**: Harsha (23f3003302)
- **Created At**: 2025-03-28T22:58:27.139Z
- **Content**:  
  Hi <a class="mention" href="/u/jivraj">@jivraj</a>,
The contents of Expected and Result matches, but still test case’s failed.<br>
Is there formatting check for answer , Isn’t prettier to be done ?<br>
I see that your expected answer isn’t formatted using prettier , am i wrong ?
eg:
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=14" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
[{‘first_name’: ‘Kevin’, ‘last_name’: ‘Allen’, ‘email’: ‘tonya41@example.com’}, {‘first_name’: ‘Kimberly’, ‘last_name’: ‘Allison’, ‘email’: ‘vmendoza@example.com’}, {‘first_name’: ‘Kathleen’, ‘last_name’: ‘Baldwin’, ‘email’: ‘amclean@example.com’}, {‘first_name’: ‘Jason’, ‘last_name’: ‘Banks’, ‘email’: ‘sharptara@example.org’}, {‘first_name’: ‘Tami’, ‘last_name’: ‘Bass’, ‘email’: ‘kristy61@example.com’}, {‘first_name’: ‘Brenda’, …
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=14" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
[<br>
{<br>
“first_name”: “Kevin”,<br>
“last_name”: “Allen”,<br>
“email”: “<a href="mailto:tonya41@example.com">tonya41@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Kimberly”,<br>
“last_name”: “Allison”,<br>
“email”: “<a href="mailto:vmendoza@example.com">vmendoza@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Kathleen”,<br>
“last_name”: “Baldwin”,<br>
“email”: “<a href="mailto:amclean@example.com">amclean@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Jason”,<br>
“last_name”: “Banks”,<br>
“email”: “<a href="mailto:sharptara@example.org">sharptara@example.org</a>”<br>
},<br>
{<br>
“first_name”: “Tami”,<br>
“last_name”: “Bass”,<br>
“email”: “<a href="mailto:kristy61@example.com">kristy61@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Brenda”,<br>
“last_name”: “Bradford”,<br>
“email”: “<a href="mailto:amandakeith@example.com">amandakeith@example.com</a>”<br>
},…
- **Reactions**: None
- **Post Number**: 31

