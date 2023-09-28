#!/usr/bin/python3

import sys


def main():
    args = sys.argv[1:]

    if not args:
        print(0)
    else:
        result = sum(map(int, args))
        print(result)


if __name__ == "__main__":
    main()
