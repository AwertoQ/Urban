import  random
def random_namber():
    fiest_namber = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    key_1 = random.choice(fiest_namber)
    return key_1

key_1 = random_namber()
key_2 = ''

for i in range(1, key_1):
    for j in range(i + 1, key_1):
        if key_1 == i + j:
            key_2 += str(i) + str(j)

print(key_1, '-', key_2)