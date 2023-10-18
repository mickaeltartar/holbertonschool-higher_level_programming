#!/usr/bin/python3
""" JSON representation """


import json


def load_from_json_file(filename):
    """ read a file with json """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
