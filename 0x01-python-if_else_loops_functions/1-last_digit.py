#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def get_last_digit(number):
    if 0 < number < 10:
        return -number
    if number < 0:
        return -get_last_digit(abs(number) // 10)
    last_digit_value = number % 10
    return last_digit_value


d = get_last_digit(number)
if d > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, d))
elif 0 < d < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, d))
else:
    print("Last digit of {} is {} and is 0".format(number, d))
