#!/usr/bin/python3

""" Module defines a square class """


class Square:
    """ Square class with private instance attr size, area method """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
