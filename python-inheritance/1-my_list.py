#!/usr/bin/python3

""" Write a class MyList that inherits from list """


class MyList(list):
    """ class Mylist """

    def print_sorted(self):
        """ inherits from list """

        if issubclass(MyList, list):
            print(sorted(self))
