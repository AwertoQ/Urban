immutable_var = 1, True, 'Age'
print(immutable_var)
# immutable_var[0] = 2 , Данная команда не может быть выполнена по причине не изменяемости данных в нутри самого кортеджа.
mutable_list = ['1', '2', '3']
print(mutable_list)
mutable_list[0] = 'aplle'
mutable_list[1] = 'banana'
mutable_list[2] = 'coconut'
mutable_list.append('4')
print(mutable_list)
mutable_list.remove('banana')
print(mutable_list)