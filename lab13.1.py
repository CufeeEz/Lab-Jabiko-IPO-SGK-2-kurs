from math import *
class Point3D():
    def __init__(self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        self.x = self.x + other
        self.y = self.y + other
        self.z = self.z + other
        return self.x, self.y, self.z
    def __sub__(self, other):
        self.x = self.x - other
        self.y = self.y - other
        self.z = self.z - other
        return self.x, self.y, self.z 
    def __mul__(self, other):
        self.x = self.x * other
        self.y = self.y * other
        self.z = self.z * other
        return self.x, self.y, self.z   
    def __truediv__(self, other):
        self.x = self.x / other
        self.y = self.y / other
        self.z = self.z / other
        return self.x, self.y, self.z
    def MinMax(self):
        print("Наименьшее число = ", min(self.x, self.y, self.z), "\nНаибольшее = ", max(self.x, self.y, self.z))
x = int(input("Введите число x ="))
y = int(input("Введите число y ="))
z = int(input("Введите число z ="))
test = Point3D(x, y ,z)
n = 1
while n == 1:
    vibor = str(input("Выберите операцию. \n+ сложение \n- вычитание \n* умножение \n/ деление\n"))
    if vibor == "+":
        num = int(input("Введите число которое надо сложить:"))
        test + num
        print(test.x, test.y, test.z)
    elif vibor == "-":
        num = int(input("Введите число которое надо вычесть:"))
        test - num
        print(test.x, test.y, test.z)
    elif vibor == "*":
        num = int(input("Введите число на которое надо умножить:"))
        test + num
        print(test.x, test.y, test.z)
    elif vibor == "/":
        num = int(input("Введите число на которое надо поделить:"))
        test + num
        print(test.x, test.y, test.z)
    else:
        print("Вы ввели неверную операцию")
    print("Желате продолжить?\n1- Да\n0 - нет")
    int(input(n))
test.MinMax()