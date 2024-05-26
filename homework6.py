my_dict = {'Anton': 1999, 'Kirill': 2001, 'Semen': 1995}
print(my_dict)
print(my_dict['Semen'])
my_dict['Artem'] = 2000
print(my_dict)
my_dict.update({'Mila': 2000, 'Alina': 1997})
print(my_dict)
del my_dict['Anton']
print(my_dict)
my_set = {1, 1, 1, 2, 3, 3, 4}
print(my_set)
my_set = [1, 1, 1, 2, 3, 4, 5, 6, (1, 3)]
my_set = set(my_set)
print(my_set.remove(1))