#!/usr/bin/python3
"""
Class Module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle subclass """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instance initialization method

        args:
            width: width of rectangle
            height: height of rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ return area of width & height """
        return self.width * self.height

    def display(self):
        """ print into stdout """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """ return value of str method """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """ width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """ height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter method """
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter method """
        self.integer_validator2('y', value)
        self.__y = value
