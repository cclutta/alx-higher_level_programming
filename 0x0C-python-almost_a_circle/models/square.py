#!/usr/bin/python3
"""Square module
Defines the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Used to initiate attributes

        Args:
            size: size of the square
            x: x attrubute
            y: y attribute
            id: class Id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get or set the width of the rectangle."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
