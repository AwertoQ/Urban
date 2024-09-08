from pprint import pprint

class Product:

    def __init__(self, Name, Weight, category):
        self.name = Name
        self.weight = Weight
        self.tupe = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.tupe}')

class Shop(Product):

    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_ = file.read()
        file.close()
        print(f'{list_}')

    def add(self, *products):
        for i in products:
            q = (str(i))
            file = open(self.__file_name, 'r')
            j = file.read()
            file.close()
            if q in j:
                print(f'Продукт {q} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{q}')
                file.close()

s1 = Shop('',0,'')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())