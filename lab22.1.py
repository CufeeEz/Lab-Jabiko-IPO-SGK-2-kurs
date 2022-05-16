import imp
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from requests import head, request
"""res = urlopen("http://mail.ru")
print(res.read(34).decode("cp1251"))
print(res.readline(100).decode("cp1251"))
print(res.readlines(1))

res1 = urlopen("http://mail.ru")
info = res.info()
info.items()
print(info)"""

"""#data = urlencode({"color":"Красный","var":15}, encoding="cp1251")
url = "http://mail.ru" + data
res1 = urlopen(url)
print(res.read(34).decode("cp1251"))"""

"""headesr = {"User-Agent": "MySpider/1.0", "Accept" : "text/html, text/plain, application/xml", "Accept-Language": "ru, ru-RU", "Accept-Charset": "windows-1251","Referer":"/index.php"}
data = urlencode({"color":"Красный", "var":15}, encoding="cp1251")
url = "http://mail.ru/testrobots.php?" + data
request = Request(url, headers=headesr)
res = urlopen(request)
print(res.read(34).decode("cp1251"))

url2 = "http://mail.ru/testrobots.php"
request = Request(url2, data.encode("cp1251"), headers=headesr)
res2 = urlopen(request)
print(res2.read(34).decode("cp1251"))"""

import chardet
chardet.detect(bytes("Строка", "cp1251"))
#chardet.detect(bytes("Строка", "utf-8"))
