#!/usr/bin/python3


def print_last_digit(n):
    if (n < 0):
        n = -n
    print(n % 10, end="")
    return n % -10
