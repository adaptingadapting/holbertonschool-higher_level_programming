#!/usr/bin/python3
""" module for creating mylist class """


class MyList(list):
    """ class mylist inherits from list and adds some bells """

    def print_sorted(self):
        print(sorted(self))
