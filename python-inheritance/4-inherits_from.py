#!/usr/bin/python3
""" module for something 2 """


def inherits_from(obj, a_class):
    """ obj class something """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
