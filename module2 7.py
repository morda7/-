def print_params(a=1, b='artem', c=True):
    print(a, b, c)

print_params()
print_params(3, 'Artem', True)
print_params(b = 25,)
print_params(c = [1,2,3])

value_list = [1, 'a', True]
value_dict = {'a': 1, 'b': [1, 2, 3], 'c': False}
print_params(*value_list)
print_params(**value_dict)

value_list2 = [123, 'Artem']
print_params(*value_list2, 42)