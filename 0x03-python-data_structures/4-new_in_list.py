#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < len(new_list) and idx >= 0:
        new_list[idx] = element
    return new_list
