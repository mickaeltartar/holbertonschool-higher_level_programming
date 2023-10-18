#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """ writing the file function """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
