import numpy as np

massiv = np.random.randint(-10, 10, size=(12))
print(massiv)
result = 0
for i in range(len(massiv)):
    if massiv[i] <= -1:
        result += massiv[i]
print(result)
