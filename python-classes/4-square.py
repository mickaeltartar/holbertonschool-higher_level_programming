#!/usr/bin/python3
"""module 4 """


class Square:
    """access and update a private attribute """
    def __init__(self, size=0):
        """ init """
        self.size = size

    @property
    def size(self):
        """ getter method to retreive """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter method to initialize value """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return the current area """
        return (self.__size ** 2)
