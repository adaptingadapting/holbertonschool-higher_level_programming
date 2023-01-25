#!/usr/bin/python3


def roman_to_int(string):
    if type(string) != str or not string:
        return 0
    dicto = {"I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(string)):
        if i > 0 and dicto[string[i]] > dicto[string[i - 1]]:
            result += dicto[string[i]]
            result -= dicto[string[i - 1]] * 2
        else:
            result += dicto[string[i]]
    return result
