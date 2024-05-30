#!/usr/bin/python3

""" File name : 6-base_geometry.py
    It is not allowed to import any module
"""


class BaseGeometry(object):
    """Define class base geometry"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Define class base geometry"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
