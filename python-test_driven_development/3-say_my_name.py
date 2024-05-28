#!/usr/bin/python3
"""
This module is composed of a function that prints a name.
"""


def say_my_name(first_name, last_name=""):
    """Return string with full name
    first_name and last_name must be strings
    Raises:
        TypeError: first_name must be a string
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
