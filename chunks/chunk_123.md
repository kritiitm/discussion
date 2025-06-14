### Post 110
**Post URL**: /t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/110
- **ID**: 585252
- **Author**: Saravanan (sarvan108)
- **Created At**: 2025-01-25T22:44:44.192Z
- **Reply To**: Post 50 (Siva Bhaskaran, siva.bhaskaran)
- **Content**:  
  I ran this directly in the console and got the correct answer.
// Select all <div> and <span> elements with the ‘foo’ class<br>
const fooElements = document.querySelectorAll(“div.foo, span.foo”);
// Initialize a variable to store the sum<br>
let sum = 0;
// Iterate through the selected elements<br>
fooElements.forEach(element =&gt; {<br>
// Get the ‘data-value’ attribute and convert it to a number<br>
const value = parseFloat(element.getAttribute(“data-value”));
// Add the value to the sum<br>
if (!isNaN(value)) {<br>
sum += value;<br>
}<br>
});
console.log(“Sum of data-value attributes:”, sum);</span></div>
- **Reactions**: None
- **Post Number**: 110

