#!/usr/bin/env python3
import sys

def multiplication_table(m):
    for column in range(1, n + 1):
        for row in range(1, n + 1):
            print(column*row, end='\t')
        print()

n = int(sys.argv[1])
multiplication_table(n)
