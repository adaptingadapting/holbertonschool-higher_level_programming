#!/usr/bin/python3
""" defines a student class """


class Student:
    """ student class with various attributes """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and\
           all(type(element) is str for element in attrs):
            new_dict = {}
            di = self.__dict__
            for key, value in di.items():
                for elements in attrs:
                    if key == elements:
                        new_dict.update({key: value})
            return new_dict
        else:
            return self.__dict__
