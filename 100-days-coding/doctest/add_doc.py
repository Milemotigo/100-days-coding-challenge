#!/usr/bin/python3
def add(a, b):
    ''' documentation fo add function
    >>> add(6, 7)
    13.0
    >>> add(6.1, 7.0)
    13.1
    '''
    return float(a + b)

def greet(value='world'):
    '''
    >>> greet('alann')
    hello, alann!
    >>> greet()
    hello, world!
    '''
    print(f'hello, {value}!')

if __name__ == "__main__":
    doctest.testmod()
