#!/usr/bin/python3
"""
This module contains a function that reads a text file (UTF-8) and
prints its contents to stdout.
"""


def read_file(filename=""):
    """Read a text file (UTF8) and print its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
