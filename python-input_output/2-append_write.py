#!/usr/bin/python3
"""
appends a string at the end of a text
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
