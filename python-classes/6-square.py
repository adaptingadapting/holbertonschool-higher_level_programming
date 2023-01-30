#!/usr/bin/python3

""" Square class with size, has area and print methods """


class Square:
    """ Squares size, will be checked for with the setter """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif not value >= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(self.__position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in self.__position:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2\
                positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print()
            return
        for h in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for e in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
