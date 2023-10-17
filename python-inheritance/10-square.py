#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """ classe square """

    def __init__(self, size):
        """ init square """

        self.__size = size

        self.integer_validator("size", size)

        super().__init__(size, size)

    def area(self):
        """ define an area """
        return self.__size ** 2
