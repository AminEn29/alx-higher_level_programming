#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    if idx >= a or idx < 0:
        return my_list
    b = my_list[:]
    b[idx] = element
    return b
