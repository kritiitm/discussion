### Post 3
**Post URL**: /t/solving-roe-realtime/168943/3
- **ID**: 602184
- **Author**: Andrew David (23f1002382)
- **Created At**: 2025-03-02T08:05:59.474Z
- **Content**:  
  Q^: 6 Move and rename files (1 mark)
Download q-move-rename-files.zip and extract it. Use <code>mv</code> to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, <code>a1b9c.txt</code> becomes <code>a2b0c.txt</code>.
ANSWER:
<pre><code class="lang-auto">unzip /workspaces/TDS/q-move-rename-files.zip -d extracted_folder123123
    5  mkdir empty_folder 
    6  find extracted_folder -type f -exec mv {} empty_folder/ \; 
    7  ls
    8  find extracted_folder123123 -type f -exec mv {} empty_folder/ \; 
    9  cd empty_folder  
   10  for file in *; do       new_name=$(echo "$file" | tr '0123456789' '1234567890')  ;     mv "$file" "$new_name"  ; done  
   11  grep . * | LC_ALL=C sort | sha256sum  
</code></pre>
- **Reactions**: None
- **Post Number**: 3

