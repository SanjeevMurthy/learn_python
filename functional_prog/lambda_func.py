def multiply(item):
    return item * 2


lst = [1, 2, 3]
print(list(map(multiply, lst)))

"""
lambda syntax
> lambda param : action(param)
"""
print(list(map(lambda item: item * 2, lst)))

my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# Sorting
un_sorted = [(0, 2), (4, 3), (9, 9), (10, -1)]

#un_sorted.sort()

un_sorted.sort(key=lambda x: x[1])

print(un_sorted)
