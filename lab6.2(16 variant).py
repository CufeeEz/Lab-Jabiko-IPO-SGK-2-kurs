from random import *
a = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],]
up = 0
down = 0
for i in range(5):
    for j in range(5):
        a[i][j] = randint(1,40)
for i in range(5):
    print(a[i])
for i in range(5):
    for j in range(5):
        if (j > i):
            up += a[i][j]
        if (j < i):
            down += a[i][j]
print("Сумма элементов расположенных над главной диагональю =", up)
print("Сумма элементов расположенных под главной диагональю =", down)

