#!/usr/bin/pythoon 
def print_reversed_list_integer(my_list=[]):
    a, c = len(my_list), 0
    for b in range(a):
        c = my_list[a - 1]
        print("{:d}".format(c))
        a = a - 1