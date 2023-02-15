#!/usr/bin/python3
""" module deifnes a class """


class Base:
    """ class is defined here """

    __nb_objects = 0

    def __init__(self, id=None):
        """ documentation """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ documentation """

        import json

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ documentation """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ documentation """

        import json

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ documentaton """

        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ documnetation """

        import json

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename) as jfile:
                r_list = Base.from_json_string(jfile.read())
                return [cls.create(**d) for d in r_list]
        except IOError:
            return []
