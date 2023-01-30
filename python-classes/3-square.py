#!/usr/bin/python3

""" Square class with size and area """


class Square:
    """ Square class with optional instance attribute size and
area calculation method """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
