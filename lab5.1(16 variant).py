from random import *
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    a[i] = randint(-20,40)
print(a)
for i in range(10):
    if a[i] >= 0:
        a[i] = a[i] / 2
    if a[i] < 0:
         a[i] = i
print(a)         
