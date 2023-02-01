#!/usr/bin/python3

""" module for defining the rectangle class """


class Rectangle:
    """ Rectangle class defines a class and its attributes and methods """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        new_string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new_string += str(self.print_symbol)
            if i < self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        return "Rectangle(" + str(self.__height) +\
            ", " + str(self.__width) + ")"

    def __del__(self):
        print("Bye rectangle")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        return rect_2

    def square(cls, size=0):
        new = Rectangle(size, size)
        return new


Rectangle.square = classmethod(Rectangle.square)
Rectangle.bigger_or_equal = staticmethod(Rectangle.bigger_or_equal)
