#!/usr/bin/python3
"""
MyInt Module
Defines my int class that inherits int
"""


class MyInt(int):
    """ MyInt class. """

    def __eq__(self, other):
        """ == behavior """
        return int(self) != other

    def __ne__(self, other):
        """ != behavior """
        return int(self) == other
