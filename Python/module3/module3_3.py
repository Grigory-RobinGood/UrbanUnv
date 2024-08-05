def print_params(a: object = 1, b: object = 'string', c: object = True):
    print(a, b, c)


print_params(1, 2, 3)
print_params(None, True, 35.8)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

values_list = [15, True, 'num']
values_dict = {'a': 18, 'b': 'run', 'c': False}

print_params(values_list, values_dict)

values_list_2 = ['buble', 25.4]

print_params(*values_list_2, 45)
