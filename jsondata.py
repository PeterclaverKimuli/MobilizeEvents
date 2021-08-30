import requests
import json
from flask import jsonify

class ImportJson():

	posts = requests.get('https://api.mobilize.us/v1/events')
	posts = posts.json()

	# url_1 = "http://127.0.0.1:5000/home"

	# payload_1 = json.dumps(response)

	# headers_1 = {'Content-Type': 'application/json'}

	# response_1 = requests.request("POST", url_1, headers=headers_1, data=payload_1)




