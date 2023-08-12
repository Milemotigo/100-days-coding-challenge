#!/usr/bin/python3

my_dict = {
    'name': 'favour',
    'spec': 'soft_w',
    'level': 'junior'
}

for key, val in my_dict.items():
    print(key, val)

def put(key, value):
    for k, v in my_dict.items():
        if k not in my_dict:
            my_dict[key] = value
            print(my_dict)

put('yell', 'chatgpt')
