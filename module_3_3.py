def print_params(a = 1, b = 'строка', c = True):
        print(a, b, c)

print_params()
print_params(15)
print_params('one', 5,)
print_params(3, 5, 8)
print_params(b=25)
print_params(c=[1,2,3])


values_list = ['Wonderful', 3.14, True]
values_dict = {'a': 5, 'b': False, 'c': 'ok'}

print_params(*values_list)
print_params(**values_dict)


values_list_2 = [1, 'two']

print_params(*values_list_2)