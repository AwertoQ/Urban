class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.num_ = number_of_floors

    def __len__(self):
        return self.num_

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_}'

    def go_to(self ,new_flore):
        self.new_flore = new_flore
        if new_flore < 1 or new_flore > self.num_:
            print('Tакого этажа не существует')
        else:
            for i in range(1, new_flore + 1):
                print(f'Прибыли на этаж {i}')

    def __eq__(self, other):  # Начало module_5_3
        return self.num_ == other
    def __lt__(self, other):
        return self.num_ < other
    def __le__(self, other):
        return self.num_ <= other
    def __gt__(self, other):
        return self.num_ > other
    def __ge__(self, other):
        return self.num_ >= other
    def __ne__(self, other):
        return self.num_ != other

    def __add__(self, value):
        return self.num_ + value
    def __radd__(self, value):
        return value + self.num_
    def __iadd__(self, value):
        return self.num_ + value




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

h1 = House('ЖК Эльбрус', 10)  # Исходные данные для module_5_3
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__