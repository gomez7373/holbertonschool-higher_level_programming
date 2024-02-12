#!/usr/bin/python3
"""
   Class BaseGeometry, Public instance method: \
   def area(self): that raises an Exception with\
   the message area() is not implemented.
"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Public instance method: def area(self): \
           that raises an Exception with\
           the message area() is not implemented."""
        raise Exception("area() is not implemented")
