#!/usr/bin/python3
"""divemod is a funtion that will divide a given 
number and returns the result and rmainder in this format 100/30 = (3, 3)
"""
import sys

def div(num1, num2):
    if len(sys.argv) <= 1:
       print("provide a number and a divisor")
    arg1, arg2 = divmod(num1, num2)
    print("{}:{}". format(arg1, arg2))

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
div(num1, num2)