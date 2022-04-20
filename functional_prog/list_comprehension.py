"""
Syntax
[<Expression> <loop> <Condition>]
"""

lst1 = [num for num in range(0,100)]

lst2 = [num for num in range(0,50) if num % 2 == 0]


print(lst1)
print(lst2)

set1 = {num for num in range(0,100)}

set2 = {num for num in range(0,50) if num % 2 == 0}

print(set1)
print(set2)