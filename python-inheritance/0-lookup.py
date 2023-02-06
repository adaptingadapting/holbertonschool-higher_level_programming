#!/usr/bin/python3
""" module for lookuing up something in a list """


def lookup(obj):
    """ lookup returns a list of the attributrs and methods """
    return list(dir(obj))
