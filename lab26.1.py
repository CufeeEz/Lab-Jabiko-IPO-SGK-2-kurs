import numpy as np

massiv = []
massiv = np.random.randint(-100, 100, size=(5))
print(massiv)
def sort(massiv):
    for i in range(len(massiv)):
        swap = i + np.argmax(massiv[i:])
        (massiv[i],massiv[swap]) = (massiv[swap],massiv[i])
    return massiv
sort(massiv)
print(massiv)

def summa(massiv):
    summ = 0
    for i in range(len(massiv)):
        summ += massiv[i]
    print(summ)
    return summ
summa(massiv)
