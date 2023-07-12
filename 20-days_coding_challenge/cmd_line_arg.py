#!/usr/bin/python3
# A funtion that takes inputs from the user in the command line

import sys

def args(name, age):
    print(f"your name is {name} and your age is {age}")

if len(sys.argv) >= 3:
    name = sys.argv[1]
    age = sys.argv[2]
    args(name, age)

else:
    print("Provide a valid input name and age")
