#!/usr/bin/python3


def uppercase(str):
    for i in str:
        i = ord(i)
        if (i >= ord("a") and i <= ord("z")):
            i -= 32
        print("{}".format(chr(i)), end="")
    print("")
