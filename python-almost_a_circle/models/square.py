#!/usr/bin/python3
""" square task """

from rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ init square method
        args: size: square size
            x: x position
            y: y position
            id: object id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ print method
        return: formated list
        """
        return ("[{}] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                              self.width))
