#does not support indexiing
my_set = {1,2,3,4,5}
my_set.add(100)
my_set.add(2)

print(my_set)

#remove duplicate values from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
print(set(my_list))


#Methods
your_set = {4,5,6,7,8,9}
print(my_set.difference(your_set))

print(my_set.difference_update(your_set))

print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))