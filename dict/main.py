user = {
    "basket":[1,2,3],
    "greet":"hello",
    'age':20
}

print(user.get('age', 55))

user2 = dict(name="sanju")

print('basket' in user)
print('greet' in user.keys())
print(user.items())

user.update({'age':55})
print(user)