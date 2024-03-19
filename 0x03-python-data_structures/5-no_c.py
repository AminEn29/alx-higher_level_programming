#!/usr/bin/python3
def no_c(my_string):
    a = my_string
    for i in range(len(a)):
        if a[i] == 'c' or 'C':
            a[i] = []
    return a