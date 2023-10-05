#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    print_num = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            print_num += 1
        except (ValueError, TypeError):
            index += 1
            continue
    print()
    return print_num
