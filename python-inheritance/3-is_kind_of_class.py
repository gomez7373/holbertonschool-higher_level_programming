#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Function returns True if object is an \
       instance of, or if object is a instance of \
       a class that inherited from, the specified class \
       ; otherwise False"""
    if isinstance(obj, a_class):
        return True
    return False
