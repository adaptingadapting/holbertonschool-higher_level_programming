#!/usr/bin/python3


def max_integer(my_list=[]):
    if not list:
        return None
    maxy = 0
    for i in my_list:
        if i > maxy:
            maxy = i
    return maxy
