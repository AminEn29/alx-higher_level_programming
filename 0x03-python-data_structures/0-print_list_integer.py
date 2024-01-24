#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a, b, c = len(my_list), 0, 0
    for b in range(a):
        c = my_list[b]
        print("{}".format(c))
        b + 1
