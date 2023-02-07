#!/usr/bin/python3
""" module for defiing the json to string class """


import json


def to_json_string(my_obj):
    """ returns the json rep of a an object string """

    return json.dumps(my_obj)
