import requests
url = 'http://pskkariatida.ru'
response = requests.get(url) # GET

data = {'user': 'tim', 'passwd': '31337'}
response = requests.post(url, data=data) # POST
print(response.content) # response.content = string; response.content = bytestring
