#!/usr/bin/python3
alphabet = ""
for char in range(97, 123):
    if chr(char) not in ['q', 'e']:
        alphabet += chr(char)
print("{}".format(alphabet), end="")
