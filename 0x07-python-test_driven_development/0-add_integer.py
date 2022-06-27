#!/usr/bin/python3
"""
add_integer module

has one function
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b
    
    Args:
        a (int, float): first number
        b (int, float): second number
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
        except:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")
        
    if type(b) in [int, float]:
        try:
            b = int(b)
        except:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")
    return a + b
