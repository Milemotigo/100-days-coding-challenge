#!/usr/bin/python3

'''practicing list comprehension'''

names = [
        'karomaro',
        'marorot',
        'pizaro',
        'pokoli'
        ]
#list comprehension
lenght = [len(name) for name in names]
print (lenght)

#Dictionary comprehension
lenght = {name:len(name) for name in names}
print (lenght)
