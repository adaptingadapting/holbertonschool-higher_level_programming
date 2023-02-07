#!/usr/bin/python3
""" module that defines a file reading mechanism """


def write_file(filename="", text=""):
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
    return len(text)
