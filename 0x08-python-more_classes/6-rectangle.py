#!/usr/bin/python3
"""Rectangle module.
This module contains a class that defines a rectangle.
"""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ Print behavior. """
        r = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                r += '#' * self.__width + '\n'
        return r[:-1]

    def __repr__(self):
        """ Repr behavior for rectangle. """
        r = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return r

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ Returns area. """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter. """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    def __del__(self):
        """ Sets del behavior of object. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
