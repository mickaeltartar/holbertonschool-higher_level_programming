#!/usr/bin/python3
""" append a text """


def append_write(filename="", text=""):
    """ function that append a text """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
