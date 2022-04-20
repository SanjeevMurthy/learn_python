# Find duplicates

lst = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 7]


def find_dup(item):
    dup_lst = []
    for i in item:
        if item.count(i) > 1:
            if i not in dup_lst:
                dup_lst.append(i)
    return dup_lst


print(find_dup(lst))

lst1 = list(set([i for i in lst if lst.count(i) > 1]))

print(lst1)
