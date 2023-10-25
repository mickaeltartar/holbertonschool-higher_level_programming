#!/usr/bin/python3
"""
Class Module
"""
import json


class Base:
    """ base class
    Attributes:
        _nb_objects: number of objects created
        id: id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiation method
        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    def integer_validator2(self, name, value):
        """check if value is an integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON string
        args:
        list dictionaries: a list of a disctionaries
        return: list of JSON string
        """
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON string in file
        args:
        list_objs: list of object
        """
        if list_objs:
            index = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            index = '[]'
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(index)
