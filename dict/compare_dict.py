master = {'0003': [
            {'register_number': 'reg26', 'mac_address': '00:2b:67:1c:b8:9a', 'cr_number': '01'},
            {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03', 'cr_number': '02'}
            ],
          '0004': [
            {'register_number': 'reg26', 'mac_address': '00:2b:67:1c:b8:9a', 'cr_number': '01'},
            {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03', 'cr_number': '02'}
          ]}

dhcp = {'0003': [
    {'register_number': 'reg24', 'mac_address': '00:2b:67:1c:bd:fb'},
    {'register_number': 'reg25', 'mac_address': '00:2b:67:1c:b9:a7'},
    {'register_number': 'reg26', 'mac_address': '00:2b:67:1c:b8:9a'},
    {'register_number': 'reg27', 'mac_address': '54:05:db:45:97:03'}
]}


def fix_master_data(data):
    for store in data:
        for reg in data[store]:
            reg.pop('cr_number')
    return data


def compare_stores(master, dhcp):
    for reg in master:
        if reg in dhcp:
            print("Equal", reg['register_number'])
        else:
            print("Non Equal", reg['register_number'])


fixed = fix_master_data(master)
#print("Fixed")
#print(fixed)

compare_stores(fixed['0003'], dhcp['0003'])


