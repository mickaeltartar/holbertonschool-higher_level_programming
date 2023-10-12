#!/usr/bin/python3
""" create a rectangle """


class Rectangle:
    """ start the class """
    def __init__(self, width=0, height=0):
        """ init rectangle

        Args:
            width: rectangle width
            height: rectangle height

        raises:
            TypeError: if width or height is not integer
            ValueError: if width or height is < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ define width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ define value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ define height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ define value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
