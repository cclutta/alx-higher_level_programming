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
        """Set the width of the square. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the rectangle attributes. """
        dct = {}
        if args is not None and len(args) > 0:
            keys = ['id', 'size', 'x', 'y']
            for i in range(len(args) if len(args) <= 4 else 4):
                dct[keys[i]] = args[i]
        else:
            dct = kwargs

        if len(dct) > 0:
            for key, value in dct.items():
                if key == 'id' and value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y
        }
