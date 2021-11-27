a = (1, -2, 3, -4, 5, -6, 7, -8, 9, -10)
s = []
proiz = 1
for i in range(10):
    if a[i] > 0:
        s.append(a[i])
lenn = len(s)

for i in range(lenn):
    proiz *= s[i]
print(lenn,"положительных элементов в списке")
print("Произведение всех элементов списка = ", proiz)