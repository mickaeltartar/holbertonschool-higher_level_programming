#!/usr/bin/python3

""" print a text with two line after ., ? and : """


def text_indentation(text):
    """ Args:
        text (str): text to be indented

        Raises:
        TypeError: if text is not a string
    """
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
