first = input()
second = input()
third = input()
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)