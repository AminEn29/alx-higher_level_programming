#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(number):
    if (number < 0):
        return (-number)
    last_digit = number % 10
    return last_digit
last = last_digit(number)
if (last > 5):
    print("Last digit of", number,"is {} and is greater than 5".format(last))
elif (last < 6 and last != 0):
    print("Last digit of", number,"is {} and is less than 6 and not 0".format(last))
else:
    print("Last digit of", number,"is {} and is 0".format(last))
    

