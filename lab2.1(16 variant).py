from math import * # math это математическая библиотека, чтобы работали формулы с косинусом, тангенсом, катангенсом и тд. импорт - подключение.
x = float(input("Введите число x: ")) # тут кароче переменной х задаем тип переменной флоат(дробные числа), инпут служит для ввода с клавиатуры числа в переменную
if 1 < x and x < 3: # тут условие, if(если) х болье 1 и 3 болье х тогла выполняются нижние строчки
    y = sqrt(x+sin(x))+1/10 # формула, препод не должен спросить про это. sqrt - это корень числа х + синус х 
    print(y) # вывод на экран резульатата 
elif x >= 3: # если число х не подходит под критерии в цикле if то будет проверятся все, что находится в elif, x больше равно 3
    y = tan(x+1) # тоже формула, тан это тангенс числа х + 1
    print(y) # вывод 
else: # если ничего из выше не подходит то выполняется все что в елсе
    print("Введено некорректное число")


