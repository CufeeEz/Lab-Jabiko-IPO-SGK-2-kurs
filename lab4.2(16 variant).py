a = str(input())
b = str(len(a))
x = ""
for i in range(int(b)):
    if ord(a[i]) > 64 and ord(a[i]) < 91:
        x += "+"
    elif ord(a[i]) > 96 and ord(a[i]) < 123:
        x += "+"
    else:
        x += a[i]
print(x)


    # A - Z = 65 - 90
    # a - z = 97 - 122
