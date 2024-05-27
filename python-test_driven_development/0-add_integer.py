#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Add 2 integers

    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer

    Return: addition of a and b

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
