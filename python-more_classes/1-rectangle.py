#!/usr/bin/python3


class Rectangle:
"""A class to represent a rectangle."""

def __init__(self, width=0, height=0):
"""Initialize a Rectangle instance with optional width and height."""
self.width = width
self.height = height

@property
def width(self):
"""int: The width of the rectangle."""
return self.__width

@width.setter
def width(self, value):
"""Set the width of the rectangle.

Raises:
TypeError: If the value is not an integer.
ValueError: If the value is less than 0.
"""

@property
def height(self):
"""int: The height of the rectangle."""
return self.__height

@height.setter
def height(self, value):
"""Set the height of the rectangle.

Raises:
TypeError: If the value is not an integer.
ValueError: If the value is less than 0.
"""
