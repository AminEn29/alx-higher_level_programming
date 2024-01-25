#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    b = my_list[:]
    b[idx] = element
    return b
