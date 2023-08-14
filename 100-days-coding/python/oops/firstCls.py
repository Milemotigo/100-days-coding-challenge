#!/usr/bin/python3
'''First class'''
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

rect1 = Rectangle(30, 40)
rect2 = Rectangle(20, 60)

print(rect1.height * rect1.width, rect2.height*rect2.width)
