#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)


def get_last_digit(number):
    if number < 0:
        return -(-number % 10)
    return number % 10


d = get_last_digit(number)

if d > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, d))
elif d < 6 and d != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
        number, d))
else:
    print("Last digit of {} is {} and is 0".format(number, d))
