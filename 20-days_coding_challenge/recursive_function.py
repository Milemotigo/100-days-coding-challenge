import sys
# recursive function in python

def recursion(r):

    if r <= 1:
        return 1
    else:
        result = (r * recursion(r - 1))
        return (result)
r = int(sys.argv[1])
print(recursion(r))
