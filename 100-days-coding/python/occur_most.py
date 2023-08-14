#!/usr/bin/python3
'''Searches for most occurence'''

lst = [1, 4, 6, 4, 8, 2, 8, 1, 4]

most = max(lst, key=lst.count)
print(most)
