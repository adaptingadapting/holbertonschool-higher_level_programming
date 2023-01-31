#!/usr/bin/python3

""" class now adds some attributes to the rectangle """


class Rectangle:
    """ class now with width and height setters """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value
