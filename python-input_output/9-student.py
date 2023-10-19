#!/usr/bin/python3
""" Write a class Student """


def __init__(self, first_name, last_name, age):
    """ Args:
            first_name(str): the first name
            last_name(str): the last name
            age(int): age
    """

    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self):
    """ retrieves a dictionary representation of a Student instance """
    return self.__dict__
