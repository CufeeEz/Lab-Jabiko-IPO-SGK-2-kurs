print('Введите три целых числа: ')
x = int(input())
y = int(input())
z = int(input())
if x > y and x > z:
    print(x, " больше всех")
elif y > x and y > z:
    print(y, "больше всех")
else:
    print(z, "больше всех")