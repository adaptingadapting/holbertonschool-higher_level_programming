#!/usr/bin/python3

""" Square class with size, has area and print methods """


class Square:
    """ Squares size, will be checked for with the setter """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or\
           not all(isinstance(num, int) for num in value) or\
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            if i < self.__size - 1:
                print()

    def __str__(self):
        self.my_print()
        return ""
