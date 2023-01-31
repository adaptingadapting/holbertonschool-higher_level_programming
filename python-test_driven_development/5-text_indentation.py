#!/usr/bin/python3

""" Module for \"indenting\" text """


def text_indentation(text):
    if not type(text) == str:
        raise TypeError("text must be a string")
    start_string = ""
    flag = 0
    for char in text:
        if not flag:
            start_string += char
        else:
            if char not in [".", "?", "!", ":", " ", "\t"]:
                start_string += char
                flag = 0
        if char in [".", "?", ":"]:
            flag = 1
            start_string += "\n" * 2
    print(start_string, end="")
