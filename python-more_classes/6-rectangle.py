#!/usr/bin/python3

""" module now also ass a few more features to the class """


class Rectangle:
    """ class now added str represanation """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        new_string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new_string += "#"
            if i < self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        retstring = "Rectangle(" + str(self.__width)
        retstring += ", " + str(self.__height) + ")"
        return retstring

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
