import numpy as np

massiv = np.random.randint(-100, 300, size=(6, 6))

print(f"{massiv}\n")
maxnum = [0 for i in range(9)] 
j = -1
for i in range(6):
    for ii in range(6):
        if i % 2 == 0:
            if ii % 2 == 0:
                j += 1
                maxnum[j] = massiv[i][ii]
print(f"Элементы массива с четными индексами\n{maxnum}\n")

print(f"Максимальный элеменет из массива с четными индексами - {max(maxnum)}")
