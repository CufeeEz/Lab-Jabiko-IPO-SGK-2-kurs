class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]
    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value
class Point:
    coordX = CoordValue()
    coordY = CoordValue()
    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y
pt = Point(1,2)
pt2 = Point(10,20)
print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)