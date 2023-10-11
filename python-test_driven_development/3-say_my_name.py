#!/usr/bin/python3
""" function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Args:

        first_name (_str_): string with the first namez
        last_name (str, optional): strung with the last name. Defaults to "".

        Raises:
            TypeError: if first_name or last_name is not a string

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
