my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
i = 0
while i < len(my_list):
    if my_list[i] > number:
        print(my_list[i])
        i += 1
    elif my_list[i] == number:
        del my_list[i]
        continue
    else:
        break