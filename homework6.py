my_dict = {'sasha': 89204562201, 'dasha': 89010154555, "misha": 88005553535}
print(my_dict)
print(my_dict['misha'])
print(my_dict.get('masha', 'Данного пользователя или номера не существует, попробуйте ещё раз!'))
my_dict.update({'nicola': 1059043456687, 'alisha': 1119043556678})
delit_name = my_dict.pop('sasha')
print(delit_name)
print(my_dict)

my_set = {1, 2, 3, 3, 4, 2, 2, 2, 1, 1, 'sasha', 'dasha', 'dasha'}
print(my_set)
my_set.update({5, 5, 'misha', 'misha'})
my_set.remove('dasha')
print(my_set)