import json

# mydict = {'UPPERCASE': 'camelValue'}
# print(mydict)
# mydict_in_str = json.dumps(mydict)
# mydict_lowercase = json.loads(mydict_in_str.lower())
# print(mydict_lowercase)

master = {'0003': [
    {'register_number': 'reg26', 'mac_address': '00:2b:67:1c:b8:9a', 'cr_number': ''},
    {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03', 'cr_number': ''},
    {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03', 'cr_number': ''},
    {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03', 'cr_number': '01'}
],
    '0004': [
        {'register_number': 'REG26', 'mac_address': '00:2B:67:1C:B8:9A', 'cr_number': '02'},
        {'register_number': 'REG27', 'mac_address': '54:05:DB:45:97:03', 'cr_number': ''}
    ],
    '0005': [
        {'register_number': 'REG26', 'mac_address': '00:2B:67:1C:B8:9A', 'cr_number': ''},
        {'register_number': 'REG27', 'mac_address': '54:05:DB:45:97:03', 'cr_number': ''},
        {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03', 'cr_number': ''}
    ]
}

for store in master:
    st = []
    for reg in master[store]:
        low_reg = dict((k.lower(), v.lower()) for k, v in reg.items())
        st.append(low_reg)
    master[store] = st

# print(master)

# dict3 = dict((k.lower(), v.lower()) for k, v in obj.items())
# print(dict3)
cr_store = {}
for store in master:
    for reg in master[store]:
        if reg['cr_number']:
            cr_store[store] = master[store]


# print("CR Store")
# print(cr_store)
#
#
# set1 = set(master)
# set2 = set(cr_store)
#
# non_cr = set1 - set2
# print(non_cr)
# print(set2)

def get_store_type(type, data):
    cr_store = {}
    for store in master:
        for reg in master[store]:
            if reg['cr_number']:
                cr_store[store] = master[store]
    cr_store_list = set(cr_store)
    non_cr_store_list = set(data) - cr_store_list
    if type == 0:
        print(cr_store_list)
    if type == 1:
        print(non_cr_store_list)


get_store_type(1, master)
