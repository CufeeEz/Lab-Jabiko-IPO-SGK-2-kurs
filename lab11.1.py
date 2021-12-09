from math import *
class Pyramid():
    def Volume(self, Ploshad, Visota):
        self.S = Ploshad
        self.h = Visota
        self.rezVolume = (self.S * self.h) / 3
    def Side(self, Kolvostr, Ploshad, Visota):
        self.n = Kolvostr
        self.S = Ploshad
        self.h = Visota
        self.rezBokPoverhnost = ((self.n * self.S) / 2) * (sqrt((self.h * self.h) + (self.s / (2 * tan(180 / self.n)))) )                        
oper = int(input("Введите желаемою операцию \n 0 - Объем пирамиды \n 1 - Объем боковой поверхности пирамиды: "))
if oper == 1 or oper == 0:
    if oper == 0:
        plos = int(input("Введите площадь основания пирамиды: "))
        vis = int(input("Введите высоту от основания пирамиды: "))
        rezul = Pyramid.Volume(0, plos, vis)
        print("Объем пирамиды = ", rezul)
    if oper == 1:
        kolstr = int(input("Введите количество сторон вашей пирамиды: "))
        plos = int(input("Введите площадь основания пирамиды: "))
        vis = int(input("Введите высоту от основания пирамиды: "))
        rezul = Pyramid.Side(0, kolstr, plos, vis)
        print("Объем боковой стороны пирамиды = ", rezul)
else:
    print("Вы ввели неверное значение!")
