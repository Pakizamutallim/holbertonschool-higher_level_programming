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

    if a == float('inf') or a == float('-inf'):
        raise OverflowError("a is too large to convert to an integer")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("b is too large to convert to an integer")

    try:
        a = int(a)
    except OverflowError:
        raise OverflowError("a is too large to convert to an integer")

    try:
        b = int(b)
    except OverflowError:
        raise OverflowError("b is too large to convert to an integer")

    return (a + b)
