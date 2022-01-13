class Cone :
    def __init__(self):
        self._length = None
        self._height = None
        self._radius = None
    def __set__(self, radius, length, height):
        print ("SideArea:", 3.14*radius*length)
        print ("Volume:", 1/3*3.14*(radius^2)*height)
    def __get__(self, radius, length, height):
        print ("SideArea:", 3.14*radius*length)
        print ("Volume:", 1/3*3.14*(radius^2)*height)
m = Cone()
print(m.__get__(5, 5, 2))
print(m.__set__(5, 5, 2))
