#!/usr/bin/python3


def add_prod(name, prod_type, category, image_source, price):
    new_prod = {
            'name':name,
            'price': price,
            'type': prod_type,
            'category': category,
            'image_source':image_source
            }
    return new_prod

name = 'laptop'
price = 1400.8
prod_type = 'electronics'
category = 'gadget'
image_source = 'example.com/images/product123.jpg'

result = add_prod(name, price, prod_type, category, image_source)
print(result)
