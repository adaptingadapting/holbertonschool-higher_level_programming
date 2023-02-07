#!/usr/bin/python3
""" module that defines a file reading mechanism """


def write_file(filename="", text=""):
    """ opens a file writes to it and returns the len of text """

    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
    return len(text)
