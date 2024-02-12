#!/usr/bin/python3
"""
    Get if a object is exactly a instance of the \
    specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Function returns True if object is\
       exactly a instance of the specified class \
       ; otherwise False"""
    if isinstance(a_class(), type(obj)):
        return True
    return False
