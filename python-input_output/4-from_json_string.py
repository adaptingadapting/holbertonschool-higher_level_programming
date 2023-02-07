#!/usr/bin/python3
""" module for turning a json strin gto an object """


import json


def from_json_string(my_str):
    """ turns a json string into object """

    return json.loads(my_str)
