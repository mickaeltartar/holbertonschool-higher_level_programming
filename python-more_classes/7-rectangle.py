#!/usr/bin/python3
""" create a rectangle """


class Rectangle:
    """ start the class """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ return area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ print a rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rectangleStr = ""
            for index in range(self.__height):
                rectangleStr += str(self.print_symbol) * self.__width + '\n'
            return rectangleStr[:-1]

    def __repr__(self):
        """ convert rectangle in string """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ delete rectangle """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
