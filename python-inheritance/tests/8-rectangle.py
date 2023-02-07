#!/usr/bin/python3
""" module for defining a rectangle class that inherits """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class that inhertis from basegeo """

    def __init__(self, width, height):
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
