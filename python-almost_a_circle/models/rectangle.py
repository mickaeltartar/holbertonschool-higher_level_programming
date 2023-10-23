#!/usr/bin/python3
""" class module """

from models.base import Base


class Rectangle(Base):
    """ subclass rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init instance method

        args:
            width: width of rectangle
            height: height of rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        self.checkFirstInteger("width", value)
        self.__width = value

    @property
    def height(self):
        """ height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        self.checkFirstInteger("height", value)
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter method """
        self.checkSecondInteger("x", value)
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter method """
        self.checkSecondInteger("y", value)
        self.__y = value
