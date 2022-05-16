from email import header
from http.client import HTTPConnection
from urllib.parse import urlencode
#con = HTTPConnection("test.ru")
#con2 = HTTPConnection("test1.ru", 80)
#con3 = HTTPConnection("test1.ru:80")

#data = urlencode({"color":"Красный","var":15},encoding="cp1251")
con = HTTPConnection("mail.ru")
con.request("GET", "")
result = con.getresponse()
print(result.read().decode("cp1251"))
con.close()
print(result.getheader("Content-Type"))
print(result.msg.get("Server"))
print(result.msg.get("X-Powered-By"))
print(result.msg.get("X-Powered-By",failobj=10))