#!/usr/bin/python3


def no_c(my_string):
    nstring = ""
    for i in my_string:
        if i != 'C' or i != 'c':
            nstring += i
    return nstring
