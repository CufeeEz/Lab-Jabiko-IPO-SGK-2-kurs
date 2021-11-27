def sr_af(massiv):
    rezultat = (massiv[0] + massiv[1] + massiv[2] + massiv[3] + massiv[4]) / 5
    print('Среднее значение 5 элементов массива = ', rezultat)
mass = [5]
print('Введите 5 целых чисел:')
for i in range(5):
    mass.append(int(input()))
sr_af(mass)

    
