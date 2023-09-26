#!/usr/bin/python3

def fizzbuzz():
    sentence = ""

    for number in range(1, 100 + 1):
        if number % 5 == 0 and number % 3 == 0:
            sentence += "FizzBuzz "
        elif number % 3 == 0:
            sentence += "Fizz "
        elif number % 5 == 0:
            sentence += "Buzz "
        else:
            sentence += str(number) + " "
    print(sentence, end="")
