#!/usr/bin/python3


""" Module creates square class with size private instance attribute """


class Square:
    """ Square with private instance attribute size """

    def __init__(self, size):
        self.__size = size
