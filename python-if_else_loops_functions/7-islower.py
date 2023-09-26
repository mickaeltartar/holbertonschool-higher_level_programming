#!/usr/bin/python3
# return 97 <= char <= 122 (same)

def islower(c):
    char = ord(c)
    lower = False
    if char >= 97 and char <= 122:
        lower = True
    return (lower)
