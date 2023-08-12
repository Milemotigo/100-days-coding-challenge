#!/usr/bin/python3
'''matching data '''
data1 = "ghhjjjhhhhhhhhsikehhdgjsh"
data2 = "ghhjjjhhhhhhhhsik7hhdgjsh"

data_zip = zip(data1, data2)

#print(list(data_zip))
enum_data = enumerate(data_zip)
#print(list(enum_data))
for i, (a,b) in enum_data:
    if a!=b:
        print(f'index:{i}')
