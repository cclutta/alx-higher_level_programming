#!/usr/bin/python3
"""MyList Module
This module contains the class MyList that inherits from list
and one method that prints the sorted list
"""


class MyList(list):
    """Defines MyList."""

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))

