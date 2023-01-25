#!/usr/bin/python3
def best_score(a_dict):
    return max(a_dict, key=lambda x: a_dict[x]) if a_dict else None
