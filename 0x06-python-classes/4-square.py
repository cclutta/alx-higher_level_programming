#!/usr/bin/python3
"""Module square
"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """ Sets private attribute size for square
        Args:
            size: size of side of square
        """
        self.__size = size

    def size(self):
        """ Returns size. """
        return self.__size

    def size(self, value):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    
    def area(self):
        """ Returns square area. """
        return self.__size ** 2
