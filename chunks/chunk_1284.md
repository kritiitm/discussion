### Post 62
**Post URL**: /t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/62
- **ID**: 591103
- **Author**: DIGVIJAYSINH SANDEEPSINH CHUDASAMA (21f2000588)
- **Created At**: 2025-02-06T06:30:07.514Z
- **Content**:  
  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
In ques 4 Scrap the BBC Weather API,<br>
I scraped the locationId for my city (i.e Mumbai)
and post that also mapped each <code>issueDate</code> to its corresponding <code>enhancedWeatherDescription</code> .
The sample output mentioned was:<br>
The output would look like this:
<pre><code class="lang-auto">{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies",
  // ... additional days
}
</code></pre>
And My Output after scraping (And as explained by professor in Video 2 BBC weather was)
{<br>
“2025-02-05”: “A clear sky and light winds”,<br>
“2025-02-06”: “A clear sky and light winds”,<br>
“2025-02-07”: “A clear sky and light winds”,<br>
“2025-02-08”: “A clear sky and light winds”,<br>
“2025-02-09”: “A clear sky and light winds”,<br>
“2025-02-10”: “A clear sky and light winds”,<br>
“2025-02-11”: “A clear sky and light winds”,<br>
“2025-02-12”: “A clear sky and light winds”,<br>
“2025-02-13”: “A clear sky and light winds”,<br>
“2025-02-14”: “A clear sky and light winds”,<br>
“2025-02-15”: “A clear sky and light winds”,<br>
“2025-02-16”: “A clear sky and light winds”,<br>
“2025-02-17”: “A clear sky and light winds”,<br>
“2025-02-18”: “A clear sky and light winds”,<br>
“2025-02-19”: “A clear sky and light winds”<br>
}
But it’s giving Error::<br>
Error: At root: Different number of properties
Can you please help how to fix this issue.
- **Reactions**: heart (1)
- **Post Number**: 62

