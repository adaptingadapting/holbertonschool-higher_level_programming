#!/usr/bin/python3
""" module deifnes a class """


class Base:
    """ class is defined here """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):

        import json

        if type(list_dictionaries) is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):

        import json

        if type(json_string) is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
