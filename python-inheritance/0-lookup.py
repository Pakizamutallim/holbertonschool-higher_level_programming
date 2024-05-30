#!/usr/bin/python3


""" File name : 0-lookup.py
    It is not allowed to import any module
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of the attributes and methods.
    """
    return dir(obj)
