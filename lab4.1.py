pro = -1
b = 0
print("Введите ваше ФИО")
fio = str(input())
x = str(len(fio))
print("Длинна строки составляет:", x) # в х стринг # int(x)
for x in range(int(x)):
    if fio[x] == fio[1]:
        pro += 1
    if fio[x] == " ":
        if fio[int(x)+1] == "В":
            b += 1
if fio[0] == "В":
    b += 1
if b > 0:
    print(b," слов начинаются на букву 'В'")
else:
    print("Нет слов начинающихся на букву 'В'")
print("Количество букв совпадающих со второй буквой фамилии:", pro)