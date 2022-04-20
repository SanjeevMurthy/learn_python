from functools import reduce


def accumulator(acc, item):
    return acc + item


my_list = [1, 2, 3, 4]
print(reduce(accumulator, my_list, 0))

print(reduce(lambda acc, item: acc + item, my_list))
