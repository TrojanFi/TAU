import json
import requests

url = "https://dog.ceo/api/breeds/image/random"
head = {'content-type': 'application/json'}
response = requests.get(url)
a = json.loads(response.text)