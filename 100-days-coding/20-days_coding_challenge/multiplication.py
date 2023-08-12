#!/usr/bin/python3
#creating a multiplication table
m = int(input("please enter a number: "))
for i in range(1, m + 1):
    for j in range(1, m +1):
        a = i*j
        print(a, end='\t')
    print()
