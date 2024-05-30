#!/usr/bin/python3

""" File name : 3-is_kind_of_class.py
    It is not allowed to import any module
"""


def inherits_from(obj, a_class):
    """inherits_from: returns True if the
    object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class) and \
        issubclass(a_class, obj.__class__) is False:
        return True
    return False