import urllib.parse
import urllib.request
url = 'http://psk-kariatida.ru'
with urllib.request.urlopen(url) as response: # GET
    content = response.read()
info = {'user': 'tim', 'passwd': '313227'}
data = urllib.parse.urlencode(info).encode()

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response: # POST
    content = response.read()
print(content)