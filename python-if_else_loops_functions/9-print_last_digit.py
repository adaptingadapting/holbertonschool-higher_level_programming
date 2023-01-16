#!/usr/bin/python3


def print_last_digit(n):
    if (n < 0):
        n = -n
    return n % -10
