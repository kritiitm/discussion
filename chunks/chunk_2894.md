### Post 4
**Post URL**: /t/graded-assignment-6/169283/4
- **ID**: 602355
- **Author**: Sarang Tambe (23f2005138)
- **Created At**: 2025-03-02T11:57:04.636Z
- **Content**:  
  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
I have similar concern<br>
For Q1, I used the following code:
<pre data-code-wrap="python"><code class="lang-python">print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')
</code></pre>
And got the following output:
<pre><code class="lang-auto">Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04
</code></pre>
Whereas options are below where none of them are correct.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png" data-download-href="/uploads/short-url/nPaaIWtriJMunrro5mxPkkzgs0I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png" alt="image" data-base62-sha1="nPaaIWtriJMunrro5mxPkkzgs0I" width="281" height="219"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">281×219 9.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Whereas for Q2 (Punjab and Yamaha) I used the following code:
<pre data-code-wrap="python"><code class="lang-python">print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') &amp; (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')
</code></pre>
and got the following answers:
<pre><code class="lang-auto">Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08
</code></pre>
The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png" data-download-href="/uploads/short-url/bEEgmsyChZ5YyAlqcLdD1S91PE2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png" alt="image" data-base62-sha1="bEEgmsyChZ5YyAlqcLdD1S91PE2" width="278" height="216"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">278×216 9.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
- **Reactions**: heart (1)
- **Post Number**: 4

