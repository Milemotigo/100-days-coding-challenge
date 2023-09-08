#!/usr/bin/python3

import product

name = 'hunder'
price = 6.7
prod_type = 'taxi'
category = 'motors'
image_source = 'https://jpg'

new = product.add_prod(name, price, prod_type, category, image_source)

print(new)
