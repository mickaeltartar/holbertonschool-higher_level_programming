#!/usr/bin/python3

def islower(c):
    char = ord(c)
    lower = False
    if char >= 97 and char <= 122:
        lower = True
    return (lower)


def uppercase(str):
    sentence = ""
    for char in str:
        if islower(char):
            upper_char = ord(char) - 32
            sentence += chr(upper_char)
        else:
            sentence += char
    print("{}".format(sentence))
