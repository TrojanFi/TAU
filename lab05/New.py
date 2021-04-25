import json


url = "https://dog.ceo/api/breeds/image/random"
head = {'content-type': 'application/json'}
response = requests.request("GET",url)
a = json.loads(response.text)