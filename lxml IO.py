from io import BytesIO
from lxml import etree

import requests

url = 'http://pskkariatida.ru'
r = requests.get(url) # GET
content = r.content # content имеет тип bytes
parser = etree.HTMLParser()
content = etree.parse(BytesIO (content), parser=parser) # преобразуем в дерево
for link in content.findall('//a'): # находим все cсылки (элемент "а")
    print(f"{link.get('href')} -> {link.text}")
