#!/usr/bin/python3
import random
number = random.randint(-10, 10)

digit = number % 10 if number >= 0 else -(-number % 10)
print("Last digit of", number, "is", digit, end=" ")

if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
