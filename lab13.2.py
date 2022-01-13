class Dog():
    __count = 0
    def __new__(self, *args, **kwargs):
        if Dog.__count<5:
            obj = super(Dog, self).__new__(self)
            return obj
        else:
            print('Не больше пяти собак!')
    def __init__(self, name, age, poroda):
        Dog.__count += 1
        self.name = name
        self.age = age
        self.poroda = poroda
dsad = Dog("fdfd", 34, "fdsfd")
dss6 = Dog("fdfd", 34, "fdsfd")
dss5 = Dog("fdfd", 34, "fdsfd")
dss4 = Dog("fdfd", 34, "fdsfd")
dss4f = Dog("fdfd", 34, "fdsfd")
sadd = Dog("dsdsd", 23, "Dsdsd")

