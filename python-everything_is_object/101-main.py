#!/usr/bin/python3
# pylint: disable=invalid-name
"""
This module defines a LockedClass that restricts dynamic attribute creation.
"""


class LockedClass:
    """
    This class prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']
