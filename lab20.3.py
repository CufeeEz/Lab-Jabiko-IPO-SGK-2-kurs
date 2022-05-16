from urllib.parse import urlparse
from urllib.parse import urlunsplit
url = urlparse("http://www.admin.ru/test.php;st?var=5#metka")
print(url)

from urllib.parse import urlunsplit
url2 = url 
urlunsplit(url)
print(url)

#res = urlopen("vk.com")