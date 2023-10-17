#!/usr/bin/python3

""" create class BaseGeometry """


class BaseGeometry:
    """ class """

    def area(self):
        """ raises an Exception with a message  """

        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name, value):
        """ validate value """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
