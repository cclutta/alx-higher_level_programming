#!/usr/bin/python3
"""
Module rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Instatiation of private attributes
        
        Args:
            width: width of rect
            height: height of rect
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, value):
        if (type) value is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
    
    @property
    def height(self):
        return self.__height
        
    @height.setter
    def height(self, value):
        if (type) value is int:
            if value >= 0:
                self.height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
