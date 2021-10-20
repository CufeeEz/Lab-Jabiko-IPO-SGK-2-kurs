from math import *
print('Введите число n: ')
n = int(input())
n += 1
for n in range(1, n):
    a = (n * n) / n ** 3 + 8
    print(a)
