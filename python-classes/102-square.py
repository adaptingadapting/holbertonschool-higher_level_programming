#!/usr/bin/python3

""" DEfines a square class and makes it comparable """


class Square:
    """ Define a square class with size attribute and area method """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other_square):
        return self.size == other_square.size

    def __neg__(self, other_square):
        return self.size != other_square.size

    def __lt__(self, other_square):
        return self.size < other_square.size

    def __le__(self, other_square):
        return self.size <= other_square.size

    def __gt__(self, other_square):
        return self.size > other_square.size

    def __ge__(self, other_square):
        return self.size >= other_square.size
