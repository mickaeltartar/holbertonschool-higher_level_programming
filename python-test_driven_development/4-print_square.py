#!/usr/bin/python3

""" print a square """


def print_square(size):
    """
    Args:
        size: length of the square
    raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print('#' * size, end="")
        print()
