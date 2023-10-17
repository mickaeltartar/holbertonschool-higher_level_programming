#!/usr/bin/python3

""" inherits my list """


class Mylist(list):
    """ my class Mylist """

    def print_sorted(self):
        """ inherits from list """
        if issubclass(Mylist, list):
            print(sorted(self))
