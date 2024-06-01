first = 123
second = 456
third = 789
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second != third:
    print('0')
first = 22
second = 44
third = 22
if first == second == third:
    print("3")
elif first == third or first == second or second == third:
    print("2")
elif first != second != third:
    print("0")
