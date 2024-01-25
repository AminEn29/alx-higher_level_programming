#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    if idx > a:
        return
    if idx < 0:
        return
    for i in range(a):
        if i == idx:
            return (my_list[i])
