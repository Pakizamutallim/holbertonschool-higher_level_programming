#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = max(a_dictionary.values())
    for key, val in a_dictionary:
        if val is None:
            return None
        if val == max_val:
            return key
