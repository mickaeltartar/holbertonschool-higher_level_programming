#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = my_list[0] if my_list else None
    for index in my_list:
        if index > max_num:
            max_num = index
    return (max_num)
