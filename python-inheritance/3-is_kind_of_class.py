#!/usr/bin/python3

""" File name : 1-my_list.py
    It is not allowed to import any module
"""


def is_kind_of_class(obj, a_class):
    """Define if a obj is instance of class"""
    if isinstance(obj, a_class):
        return True
    return False
