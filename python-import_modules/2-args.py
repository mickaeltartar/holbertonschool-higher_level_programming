#!/usr/bin/python3
import sys


def print_arguments(argv):

    numbers_of_args = len(argv)

    more_args = 's' if numbers_of_args > 1 else ''

    if numbers_of_args == 0:
        print("0 arguments.", end="\n")
    else:
        print(f"{numbers_of_args} argument{more_args}:", end="\n"
              if numbers_of_args == 1 else "\n")

    for index, arg in enumerate(argv, start=1):
        print(f"{index}: {arg}")


if __name__ == "__main__":
    args = sys.argv[1:]
    print_arguments(args)
