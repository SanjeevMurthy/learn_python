def get_odd(item):
    return item % 2 != 0


lst = [1, 2, 3]
print(list(filter(get_odd, lst)))
