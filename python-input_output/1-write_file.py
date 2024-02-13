#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF-8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8)
    and return the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    # This block is for demonstration and testing purposes.
    # Example usage:
    nb_characters = write_file("my_first_file.txt", "This School is cool!\n")
    print(nb_characters)
