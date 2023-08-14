#!/usr/bin/python3
'''Generates a secret key'''

import secrets
from sys import argv

passwd = secrets.token_hex(10)
#s1 = enumerate(passwd)
#print(list(s1))

if len(argv) < 2:
    print("Usage: python", argv[0],  "argument")
    argv.exit[1]
e = argv[1]

with open ('file.tixt', 'w') as f:
    f.write(passwd)
with open ('file.tixt', 'r') as f:
    content = f.read()
    if e in content:
        print("yes")
    else:
        print(content)
