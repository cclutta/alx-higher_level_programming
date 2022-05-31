#!/usr/bin/python3

def remove_char_at(str, n):
    c = str[:n]
    c1 = str[n+1:]
    return c + c1
