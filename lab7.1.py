z = -10
a = 1, 2, 3, 3, 3, 6, 7, 8, 9, 19
for i in range(10):
    for ii in range(10):
        if a[i] == a[ii]:
            z += 1
if z == 2:
    print("Одна пара совпадающих по значению чисел найдена")
elif z >= 6:
    print("несколько пар совпадающих по значению чисел найдена")
else:
    print("Совпадений не найдено")