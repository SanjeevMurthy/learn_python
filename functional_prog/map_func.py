def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


def multiply(item):
    return item * 2


lst = [1, 2, 3]
print(multiply_by2(lst))
print(list(map(multiply, lst)))
