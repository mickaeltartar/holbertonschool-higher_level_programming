#!/usr/bin/python3
separator = ", "
for number in range(9):
    for number0 in range(number + 1, 10):
        if number == 8 and number0 == 9:
            separator = "\n"
        print("{}{}".format(number, number0), end=separator)
