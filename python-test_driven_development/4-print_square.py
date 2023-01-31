#!/usr/bin/python3

""" module for printing square """


def print_square(size):
    """ prints a square of size size """

    if not type(size) == int:
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
