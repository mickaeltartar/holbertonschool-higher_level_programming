#!/usr/bin/python3

""" create class BaseGeometry """


class BaseGeometry:
    """ class """

    def area(self):
        """ raises an Exception with a message  """

        raise Exception(f"{self.area.__name__}() is not implemented")
