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
        self.size = size

    @property
    def size(self):
        """ Returns size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Returns square area. """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #. """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print('#' * self.__size)
