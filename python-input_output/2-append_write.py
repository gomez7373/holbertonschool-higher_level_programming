#!/usr/bin/python3
"""
Module 2-append_write contains a function that appends a string at the end
of a text file (UTF-8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    (UTF-8) and returns the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
