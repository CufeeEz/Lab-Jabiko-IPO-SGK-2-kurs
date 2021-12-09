from math import *
class PyramidVolume():
    def __init__(self, Ploshad, Visota, Kolvostr):
        self.S = Ploshad
        self.h = Visota
        self.n = Kolvostr
    def Volume(self):
        self.rezVolume = (self.S * self.h) / 3
        print("Объем пирамиды = ", self.rezVolume)
    def Side(self):
        self.rezBokPoverhnost = ((self.n * self.S) / 2) * (sqrt((self.h * self.h) + (self.S / (2 * tan(180 / self.n)))))
        print("Площадь боковой поверхности пирамиды = ", self.rezBokPoverhnost)
plos = int(input("Введите площадь основания пирамиды: "))
vis = int(input("Введите высоту от основания пирамиды: "))
kolstr = int(input("Введите количество сторон вашей пирамиды: "))
vol = PyramidVolume(plos, vis, None)
vol.Volume()
Sid = PyramidVolume(plos, vis, kolstr)
Sid.Side()
