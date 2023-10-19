#!/usr/bin/python3
""" Write a class Student """


class Student():
    """ class student """

    def __init__(self, first_name, last_name, age):
        """ Args:
                first_name(str): the first name
                last_name(str): the last name
                age(int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """

        if attrs is None:
            return self.__dict__

        if all(isinstance(attr, str)for attr in attrs):
            return {key: value for key, value
                    in self.__dict__.items() if key in attrs}
