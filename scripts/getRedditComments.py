import requests
import base64
import json



token = '' # access token here
article = '' # article ID here


urls = {
	'comments' : '/comments/'
	}
base_url = "https://oauth.reddit.com"

def get_url(url_id):
	return base_url + urls[url_id]


headers = {
		'User-Agent': 'pc:com.read.script:v0.0.1 (by /u/yourusername)',
		'Authorization': 'Bearer ' + token
	}

ret = requests.get(
	get_url('comments') + article + "?limit=5000&depth=5",

	headers=headers
	# proxies = {
	# 	'http':'http://localhost:8080',
	# 	'https':'http://localhost:8080'
	# }, verify=False
)

# from ChatGPT, get all body fields in json blob
def find_all_body_fields(data, field_name="body"):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == field_name:
                yield value
            if isinstance(value, (dict, list)):
                yield from find_all_body_fields(value, field_name)
    elif isinstance(data, list):
        for item in data:
            yield from find_all_body_fields(item, field_name)

data = json.loads(ret.text)
gezegden = find_all_body_fields(data)

with open('gezegden.txt','w') as fout:
	for x in gezegden:
		fout.write(x + "\n")

