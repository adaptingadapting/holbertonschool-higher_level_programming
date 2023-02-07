#!/usr/bin/python3
""" module for prinintg something """


import json


def save_to_json_file(my_obj, filename):
    """ writes to a file the object string """

    with open(filename, "w+") as f:
        json.dump(my_obj, f)
