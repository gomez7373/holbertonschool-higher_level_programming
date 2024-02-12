#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Function returns True if object is a \
       instance of a class that inherited (directly or \
       indirectly) from the specified class ; otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
