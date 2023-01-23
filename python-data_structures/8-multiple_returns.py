#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence or sentence == "":
            return (len(sentence), None)
    return (len(sentence), sentence[0])
