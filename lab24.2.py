import numpy as np

massiv = np.random.randint(-90, 100, size=(15, 15))
print(massiv)
maxnum = np.empty(15, dtype = int)
for x in range(15):
    for y in range(15):
        if x == y:
            maxnum[x] = massiv[x][y]
print(f"Элементы главной диагонали - \n{maxnum}\n")
maxum = max(maxnum)
print(f"Максимальный элемент главной диагонали - {maxum}\n")
dd = list(maxnum).index(maxum)
print(f"Индекс максимального числа главной диагонали - {dd},{dd}")

stroka = np.empty(15, dtype = int)
for i in range(15):
    stroka[i] = massiv[dd][i]

print(stroka)