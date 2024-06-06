#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


add_file = "add_item.json"
if path.exists(add_file):
    json_file = load_from_json_file('add_file')
else:
    json_file = []

for i in range(1, len(argv)):
    json_file.append(argv[1])

save_to_json_file(json_file, add_file)
