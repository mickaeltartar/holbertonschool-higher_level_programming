#!/usr/bin/python3

""" print a text with two line after ., ? and : """


def text_indentation(text):
    newText = ""
    needLineBreak = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    newText = text.replace(". ", ".")
    newText = text.replace("? ", "?")
    newText = text.replace(": ", ":")
    for char in newText:
        if char in [".", "?", ":"]:
            print(char)
            print()
            needLineBreak = True
        else:
            if needLineBreak is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    needLineBreak = False
