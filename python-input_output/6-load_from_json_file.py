#!/usr/bin/python3
""" module for creating an object from a json file """


import json


def load_from_json_file(filename):
    """ creates an object from a json file """

    with open(filename) as f:
        new_string = f.read()
    return json.loads(new_string)
