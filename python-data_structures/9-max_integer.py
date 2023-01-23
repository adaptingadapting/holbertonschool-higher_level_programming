#!/usr/bin/python3


def max_integer(my_list=[]):
    if not list or len(my_list) == 0:
        return None
    maxy = my_list[0]
    for i in my_list:
        if i > maxy:
            maxy = i
    return maxy
