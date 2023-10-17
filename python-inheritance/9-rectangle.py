#!/usr/bin/python3


""" a class rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ create a rectangle """

    def __init__(self, width, height):

        """ define width and height in private instance """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ return area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):

        """ print the width & the height from the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
