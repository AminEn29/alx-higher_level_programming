#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(number):
    if (number < 0):
        return (-number)
    last_digit = number % 10
    return last_digit
The_one = last_digit(number)
if (The_one > 5):
    print("Last digit  of", number,"is {} and is greater than 5".format(The_one))
elif (The_one < 6 and The_one != 0):
    print("Last digit of", number,"is {} and is less than 6 and not 0".format(The_one))
else:
    print("Last digit of", number,"is {} and is 0".format(The_one))
    

