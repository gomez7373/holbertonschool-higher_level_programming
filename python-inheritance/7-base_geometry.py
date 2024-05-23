#!/usr/bin/python3
"""This module defines a class named BaseGeometry."""

class BaseGeometry:
    """A class named BaseGeometry.

    Methods:
    - area: Raises an Exception with the message area() is not implemented.
    - integer_validator: Validates that a given value is a positive integer.
    """

    def area(self):
        """Raise an exception indicating the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that `value` is a positive integer.

        Parameters:
        - name (str): The name of the parameter (assumed to be a string).
        - value (int): The value to validate.

        Raises:
        - TypeError: If `value` is not an integer.
        - ValueError: If `value` is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
