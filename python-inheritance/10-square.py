#!/usr/bin/python3
""" Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square """

    def __init__(self, size):
        """ init a square """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ retunr area of the square """

        return self.__size ** 2
