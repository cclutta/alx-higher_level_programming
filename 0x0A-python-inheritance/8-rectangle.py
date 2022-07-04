#!/usr/bin/python3
"""Rectangle module.
This module contains a class that defines a rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
