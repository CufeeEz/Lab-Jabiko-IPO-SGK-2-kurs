q, qq, qw, name, qe, qr, ste = 0, 0, 0, 0, 0, 0, 0 # счетчики, которые будет увеличиваться
a = -1 # тоже счетчик
print("Введите ваше ФИО")
fio = str(input()) # просим ввести фио пользователя в строковом типе данных
lenn = len(fio) # присваем пременной ленн длинну строки. Функция лен считает длинну строки фио
print('Длинна строки:',lenn) # вывод значения ленн
while q < lenn: # цикл, можно было бы и использовать фор, но этим удобнее мне. Он будет выполнятся пока ленн больше q 
    if fio[1] == fio[q]:    # цикл, находящий повторения со второй буквой фамилии.
                            # в fio лежит фио, а [q] это номер буквы. 
        a += 1 # если одна из букв совпадает со второй буквой фамилии, то переменной а присваевается +1
    if fio[q] == " ": # цикл, переберающий все буквы от првой до последней, и находит пробел
        qw += 1 # если пробел был найдет то переменной присвается +1,
                # это надо для того, чтобы не выводилась сначала фамилия и отчество а потом отчество 
        if qw == 1: # если пробел был найден один раз, то он выводит
            print(fio[1+q::]) # строку фио начиная с пробела - q и до конца. + 1 надо чтобы он не выводил вместе с ИО пробел 
    q +=1 # счетчику присвается +1
if a > 0: # проверяется, есть ои в а что-нибудь
    print(a, "совпадений со второй буквой фамилии")
else: # если же ничего не найдено, то выводится ниже
    print('Не найдено совпадений со второй буквой фамилии')
while qq < lenn: # цикл на вывод количества буквв имени
    if fio[qq] == " ": # находит в фио пробел
        ste += 1 # эта штука тоже нужна для того, чтобы найти начала и конец имени. Тут мы если найден был пробел то присваеваем +1
        if ste == 1: # если был найден первый пробел, то
            qe = qq # записываем номер пробела в переменную
        if ste == 2: # если был найден второй пробел, то 
            qr = qq # записываем номер пробела в переменную
    qq +=1 # чтобы счетчик шел 
if qr == 0 or qe == 0: # проверка, если в qe или qr есть 0 то выведет ошибку
    print("Ошибка, посчитать длинну имени невозможно")
else: # в ином случае
    print("Длинна вашего имени =", (qr - qe)-1) # (qr - qe)-1 вычитывает чилсо конца имени от количества начала, и получаем длинну имя.
# Единственно он не может посчитать количество совпадений со второй буквой фамилии с началом имени или отчества, так как 
# Юникод маленького числа не равняется юникоду большого числа. 
# Советую просто писать все маленькими буквами, тогда проблем не будет