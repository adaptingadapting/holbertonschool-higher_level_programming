#!/usr/bin/python3


def roman_to_int(roman_string):
    result = 0
    roman_dict = {"X": 10, "V": 5, "D": 500, "C": 100,
                  "I": 1, "L": 50, "M": 100}
    for i in range(1, len(roman_string)):
        if roman_dict[roman_string[-i]] > roman_dict[roman_string[-i - 1]]:
            result += roman_dict[roman_string[-i]]\
                - roman_dict[roman_string[-i - 1]]
            i += 1
        else:
            result += roman_dict[roman_string[-i]]
    if len(roman_string) == 1 or\
       roman_dict[roman_string[1]] < roman_dict[roman_string[0]]:
        result += roman_dict[roman_string[0]]
    return result
