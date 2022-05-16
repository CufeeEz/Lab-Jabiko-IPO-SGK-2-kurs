from urllib.parse import urlparse
url = urlparse("http://www.admin.ru/test.php;st?var=5#metka")
print(url)