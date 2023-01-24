#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    sorte = sorted(keys)
    for i in sorte:
        print("{}: {}".format(i, a_dictionary.get(i)))
