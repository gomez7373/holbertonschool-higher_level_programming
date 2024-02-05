#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Prototype: def say_my_name(first_name, last_name="")
    first_name and last_name must be strings otherwise, raise a TypeError exception
    with the message 'first_name must be a string or last_name must be a string'.
    You are not allowed to import any module
    """

    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    # Print the formatted string
    print("My name is {} {}".format(first_name, last_name))

# Example usage
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")

# Uncomment the following line to see the exception message
# say_my_name(12, "White")
