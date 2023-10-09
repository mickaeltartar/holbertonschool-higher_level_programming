#!/usr/bin/python3
"""module 6
"""


class Square:
    """Access and update private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """init square"""
        self.size = size
        self.position = position

    @property
    def size(self):

        """def size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):

        """def value and raise exceptions for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        """def position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):

        """def value and raise exception for positon"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """return the current square"""
        return (self.__size ** 2)

    def my_print(self):

        """print a square"""
        if self.size == 0:
            print()
        else:
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end="")
                print("#" * self.size)
