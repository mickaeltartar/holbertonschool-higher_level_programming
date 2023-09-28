#!/usr/bin/python3

for index in range(0, 26, 2):
    print("{:c}{:c}".format(122 - index, (122 - index - 1) - 32), end='')
