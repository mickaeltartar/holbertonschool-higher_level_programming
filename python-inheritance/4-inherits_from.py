#!/usr/bin/python3
""" returns True if the object is an instance otherwise False """


def inherits_from(obj, a_class):
    """ return class if is instance or not """

    return isinstance(obj, a_class) and not issubclass(a_class,obj.__class__)
