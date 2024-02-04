#!/usr/bin/python3
class Square:
    """
    Defines a square with a private instance attribute: size.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """Instantiation with size (no type/value verification)."""
        self.__size = size
