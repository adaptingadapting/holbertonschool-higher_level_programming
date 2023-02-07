#!/usr/bin/python3
""" module for defining the student class """


class Student:
    """ class studnet defines a student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and\
           all(type(element) is str for element in attrs):
            new_dict = {}
            for key, value in self.__dict__.items():
                for element in attrs:
                    if key == element:
                        new_dict.update({key: value})
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            if key == "age":
                self.age = value
            if key == "last_name":
                self.last_name = value
