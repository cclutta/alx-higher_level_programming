#!/usr/bin/python3
"""Module square
"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
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

    @property
    def position(self):
        """ Returns position. """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position """
        if type(value) is tuple and len(value) is 2 and \
        type(value[0]) is int and type(value[1]) is int and \
        value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Returns square area. """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character #. """
        if self.__size > 0:
            for i in range(self._position[1]):
                print("")
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print("")
