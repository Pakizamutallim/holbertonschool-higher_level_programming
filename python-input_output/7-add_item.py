#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list,
and then saves them to a file in JSON format.
"""


from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Check if the file exists
if path.exists('add_item.json'):
    # Load existing content
    obj_json_file = load_from_json_file('add_item.json')
else:
    # Initialize an empty list if the file doesn't exist
    obj_json_file = []

# Append new arguments to the list
for i in range(1, len(argv)):
    obj_json_file.append(argv[i])

# Save the updated list back to the file
save_to_json_file(obj_json_file, 'add_item.json')
