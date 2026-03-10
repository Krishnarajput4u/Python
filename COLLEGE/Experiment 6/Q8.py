check_same = lambda d: len(set(d.values())) == 1

my_dict = {'a': 10, 'b': 10, 'c': 10}

print(check_same(my_dict))