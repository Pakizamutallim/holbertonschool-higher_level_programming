#!/usr/bin/python3
"""defines a square"""


class Square:
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            print("size must be >= 0")
            raise ValueError
