#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items_to_jason():
    """ add items """

    try:
        item_list = load_from_json_file('add_item.json')

    except FileNotFoundError:
        item_list = []

    item_list.extend(sys.argv[1:])
    save_to_json_file(item_list, "add_item.json")


if __name__ == "__main__":
    add_items_to_jason()
