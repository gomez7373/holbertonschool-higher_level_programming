#!/usr/bin/python3
"""Defines the class Square that represents the square, with the size validation."""


class Square:
    """class that defines the square by its size, with a validation."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
