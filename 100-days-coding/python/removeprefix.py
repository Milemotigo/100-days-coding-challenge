#!/usr/bin/python3
'''This function removes prefix as stated'''
links = [
        'www.google.com',
        'www.wikipedia.com',
        'www.gjs.com'
        ]
def remove_prefix():
    for link in links:
        rm = link.removeprefix('www.')
        print('removes prefix')
        print (rm)
        print('removes postfix')
        if link.endswith('.com'):
            link = link[:-4]
            post = link.remove_postfix(link)
            print(post)

remove_prefix()
