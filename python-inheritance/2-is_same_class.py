#!/usr/bin/python3
""" function that returns True if the object is exactly an instance """


def is_same_class(obj, a_class):
    """check if instance of class

    Args:
        obj (any) object to check
        a_class (any): given object

    Returns:
        booleen: true if type is instance or false if not
    """
    return type(obj) == a_class
