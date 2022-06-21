#!/usr/bin/python3
"""Module square
"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """ Sets private attribute size for square

        Args:
            size: size of side of square

        Raises:
            TypeError: when not int
            ValueError: when less than 0
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
