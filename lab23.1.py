import numpy as np
massiv = np.arange(36).reshape(6,6)
#massiv2 = np.random.randint(10, size=(6, 6))
print(massiv)
#print(massiv2)
for i in range(6):
    for j in range(6):
        if i == 0:
            massiv[i][j] = 1
        if j == 0:
            massiv[i][j] = 1
        if j == 5:
            massiv[i][j] = 1
        if i == 5:
            massiv[i][j] = 1
        if i != 0 and i !=5 and j != 0 and j !=5:
            massiv[i][j] = 0
print(massiv)