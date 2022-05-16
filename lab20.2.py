from urllib.parse import unquote, quote_from_bytes
s = quote_from_bytes(bytes("Строка1", encoding="cp1251"))
print(s)
print(unquote(s, encoding="cp1251"))
