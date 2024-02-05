#!/usr/bin/python3


def print_square(size):
    """
    Prints a square with the character #.

    Prototype: def print_square(size)
    size is the size length of the square.
    size must be an integer, otherwise raise a TypeError exception with the message
    'size must be an integer'.
    If size is less than 0, raise a ValueError exception with the message 'size must be >= 0'.
    If size is a float and is less than 0, raise a TypeError exception with the message
    'size must be an integer'.
    You are not allowed to import any module.
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    # Check if size is less than 0
    if size < 0:
        raise ValueError('size must be >= 0')

    # Check if size is a float
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    # Print the square
    for _ in range(size):
        print("#" * size)

# Example usage
print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")

# Uncomment the following line to see the exception message
# print_square(-1)
