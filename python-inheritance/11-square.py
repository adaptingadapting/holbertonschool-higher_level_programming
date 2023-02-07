#!/usr/bin/python3
""" module for definig a class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ square inherits from rectangle """

    def __init__(self, size):
        Square.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
