#!/usr/bin/python3
""" module for something """


def is_kind_of_class(obj, a_class):
    """ is kind of class """

    return isinstance(obj, a_class) or type(obj) is a_class
