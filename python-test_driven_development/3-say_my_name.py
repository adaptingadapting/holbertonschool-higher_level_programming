#!/usr/bin/python3

""" Module that prints your name """


def say_my_name(first_name, last_name=""):
    """ module that prints both names """
    if type(first_name) != str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
