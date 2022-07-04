#!/usr/bin/python3
"""Module square
Has area method
"""

Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """ Sets private attribute size for square

        Args:
            size: size of side of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns area. """
        return self.__size ** 2
