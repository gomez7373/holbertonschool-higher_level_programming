#!/usr/bin/python3
"""This module creates a class named BaseGeometry"""


class BaseGeometry:
    """A class named BaseGeometry

    Attributes:
    attr1(area): Raises an exception
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
