import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def decode(string):
	this_string = string
	decode_string = ['<', '"', '\'', '>', '&',]
	encode_string = ['&lt;', '&quot;', '&#039;', '&gt;', '&amp;']
	for e_string, d_string in zip(encode_string, decode_string):
		this_string = this_string.replace(e_string, d_string)
	for e_string, d_string in zip(encode_string[::-1], decode_string[::-1]):
		this_string = this_string.replace(e_string, d_string)
	return this_string

def encode(string):
	this_string = string
	decode_string = ['&lt;', '&quot;', '&#039;', '&gt;', '&amp;']
	encode_string = ['<', '"', '\'', '>', '&',]
	for e_string, d_string in zip(encode_string, decode_string):
		this_string = this_string.replace(e_string, d_string)
	for e_string, d_string in zip(encode_string[::-1], decode_string[::-1]):
		this_string = this_string.replace(e_string, d_string)
	return this_string

def google(keyword, cookie):
	this_search = []
	url = "https://developers.facebook.com/tools/debug/echo/?q=https%3A%2F%2Fgoogle.com%2Fsearch?q%3D"+quote(encode(keyword))+"%26num%3D1000"
	headers = {
	    'Host': 'developers.facebook.com',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Accept-Encoding': 'deflate',
	    'Connection': 'keep-alive',
	    'Cookie': cookie,
	    'Upgrade-Insecure-Requests': '1',
	    'Cache-Control': 'max-age=0',
	    'TE': 'Trailers'
	    }
	google_search = requests.get(url, headers=headers)
	cleaned_response = decode(google_search.text)
	soup = BeautifulSoup(cleaned_response, 'html.parser')

	for perlink in soup.select('.kCrYT a'):
		try:
			this_per = {}
			find_url = perlink.get('href').strip('/url?q=')
			delimeter_url = find_url.find('&')
			this_per['url'] = find_url[0:delimeter_url]
			this_per['title'] = perlink.select('.vvjwJb')[0].text
			this_search.append(this_per)
		except:
			pass
	return this_search
