#!/usr/bin/python3
separator = ", "
for number in range(0, 100):
    if number == 99:
        separator = "\n"
print("{:02d}".format(number), end=separator)
