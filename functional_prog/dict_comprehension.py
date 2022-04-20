simple_dict = {
    'a': 1,
    'b': 2
}

new_dict = {k: v for k, v in simple_dict.items() if v % 2 == 0}

print(new_dict)
