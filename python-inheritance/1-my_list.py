#!/usr/bin/python3
""" File name : 1-my_list.py
    It is not allowed to import any module
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
