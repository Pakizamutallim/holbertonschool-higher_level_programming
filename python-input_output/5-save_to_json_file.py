#!/usr/bin/python3

"""
save_to_json_file writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (json.dump(my_obj, f))
