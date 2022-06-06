#!/usr/bin/python3


def element_at(my_list, idx):
    a = len(my_list)
    for i in range(0, a):
        if i == idx:
            return my_list[i]
    return None

       
