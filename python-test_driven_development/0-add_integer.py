#!/usr/bin/python3

"""
function that add two numbers
"""


def add_integer(a, b=98):

    """_summary_

    Args:
        a (int): number
        b (int, optional): number set defaults to 98.

    Raises:
        TypeError: if a or b is not a int

    Returns:
        int: result a + b
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
