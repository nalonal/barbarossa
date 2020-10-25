<h1 align="center">
  <br>
  <a href="https://github.com/nalonal/barbarossa"><img src="https://i.ibb.co/fDctKnK/199-1998983-pirates-logo-png-download-transparent-png.png" width="400px" alt="barbarossa"></a>
  <br>
  Barbarossa
  <br>
</h1>

# Barbarossa
Python Google Crawler
<h2>Python Google Crawler</h2>
<p>Simple script to crawling google using <a href="https://developers.facebook.com/tools/debug/echo/?q=">Facebook Developers Tools Debug</a></p>

### Introduction
I learn to create simple code to crawling google search. I get inspired from [s0md3v](https://github.com/s0md3v/goop), but i use another technique to parse the code. By the way thankyou very much to share great code. So basicly this tools srape Google using Facebook [debugger tool](https://developers.facebook.com/tools/debug/echo/?q=https://example.com). This tools can scrape google search results without being blocked by the CAPTCHA. This tools also no need delay time to scrape. Love it.

### Usage
#### Installation
```
pip install barbarossa
```
#### Get Facebook Cookie
open [Facebook Developers Tools](https://developers.facebook.com/tools/) in browser and press Ctrl+i or Ctrl+Shift+i
![enter image description here](https://i.ibb.co/zPjp4WT/cookie.png)

#### Tools Use
```python
from barbarossa import google

google(cookie,keyword,maximum_search)

```

#### Example

```python
from barbarossa import google

## open www.facebook.com -> ctrl+i -> cookies
cookie = "sb=OwcgXgyAui-CPqDVkZAhxwhA; datr=OwcgXvNPvDYHpjgSs4GkOMze; c_user=100049274942399; spin=r.1002851056_b.trunk_t.1603205641_s.1_v.2_; xs=50%3AfZ5JGz_Qr9E4Mw%3A2%3A1591497132%3A5175%3A9658; fr=06MpaT9reOkXP6moa.AWUkVfrOG6zdu7jE14-6wteySKQ.BffoDv.2R.F9-.0.0.Bfjv-p.AWXfh08q1OA; wd=980x969"

for info in google(cookie,"How to use barbarossa", 10):
	print(info)

```
### Legal & Disclaimer
Scraping google search results is illegal. This library is merely a proof of concept of the bypass. The author isn't responsible for the actions of the end users.
