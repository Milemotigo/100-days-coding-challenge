#!/usr/bin/env python3
import sys
# create a lambda funtion that takes a give number and multiply it with any other number

def compute(n):
    result = lambda x : x * n
    return('Double of the given number is',result(x))
n = int(sys.argv[1])
x = int(sys.argv[2])
print(compute(n))
