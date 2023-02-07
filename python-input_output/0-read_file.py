#!/usr/bin/python3
""" module for reading a file """


def read_file(filename=""):
    """ reads a file and prints it to the stdout """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
