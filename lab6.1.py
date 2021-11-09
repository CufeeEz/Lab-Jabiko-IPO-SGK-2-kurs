from random import *
a = [[0,0,0,0,0], 
    [0,0,0,0,0], 
    [0,0,0,0,0], 
    [0,0,0,0,0], 
    [0,0,0,0,0]]
z = []
y = []
for i in range(5):
    for ii in range(5):
        a[i][ii] = randint(1,40)
        if i % 2 == 0 and ii % 2 == 0:
            z.append(a[i][ii])
        if i % 2 == 1 and ii % 2 == 1:
            y.append(a[i][ii])
print(a)
z.sort()
print(z)
y.sort(reverse=True)
print(y)