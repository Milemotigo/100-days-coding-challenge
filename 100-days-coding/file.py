#!/usr/bin/python3

with open('text.txt', 'r') as f:
    #for contents in f:
    #contents = f.read()
    contents = f
    while contents < 10:
        print(contents)
    contents = f.read()
