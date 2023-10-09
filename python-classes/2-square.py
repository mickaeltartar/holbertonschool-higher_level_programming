#!/usr/bin/python3
"""module 0
"""


class Square:
    """new square and size of him
    add condition for value and type
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
