#!/usr/bin/python3

""" Takes two ints a and returns their sum """


def add_integer(a, b=98):

    """ If a doesnt exist or a or b is not int or float\
    raise an exception """

    if not a or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
