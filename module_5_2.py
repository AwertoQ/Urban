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