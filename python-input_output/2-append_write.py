#!/usr/bin/python3
""" module for appending to a file """


def append_write(filename="", text=""):
    """ function appends to a file text """

    with open(filename, "a+", encoding="utf-8") as f:
        f.write(text)

    return len(text)
