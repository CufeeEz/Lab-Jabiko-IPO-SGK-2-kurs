from abc import ABC, abstractmethod
class Toy(ABC):
    #@abstractmethod
    def get_info(self):
        print('Информация об игрушке...')
    def search(self,color):
        if color.lower() in self.color.lower():
            return True
        return False
class Kubik(Toy):
    def __init__(self, color, cost, material, sizerebra):
        self.color=color
        self.cost=cost
        self.material=material
        self.sizerebra=sizerebra
    def get_info(self):
        return ('Кубик, Цвет: "{}"\nСтоимость: {}\nМатериал: {}\nРазмер ребра: {} '.
    format(self.color, self.cost, self.material, self.sizerebra))
class Myachik(Toy):
    def __init__(self, cost, color, diametr, material):
        self.color=color
        self.cost=cost
        self.material=material
        self.diametr=diametr
    def get_info(self):
        return ('Мячик, Стоимость: "{}"\nЦвет: {}\nДиаметр:\nМатериал:'.
    format(self.cost, self.color, self.diametr, self.material))
class Car(Toy):
    def __init__(self, username, cost, made, color):
        self.username=username
        self.cost=cost
        self.made=made
        self.color=color
    def get_info(self):
        return ('Машина, Название: "{}"\nСтоимость: {}\nПроизводитель: {}\nЦвет: {}'.
    format(self.username, self.cost, self.made, self.color))
toys=[]
toys.append(Kubik("Красный", "1000$", "Пластик", "5см"))
toys.append(Myachik("1000$", "Зеленый", "20см", "Резина"))
toys.append(Car("BMW X5 2020г.", "5000$", "Германия", "Черный"))
for toy in toys:
    print(toy.get_info())
print()
search_word = ""
print('Результаты поиска по запросу "{}": '.format(search_word))
for toy in toys:
    if toy.search(search_word):
        print(toy.get_info())
print()