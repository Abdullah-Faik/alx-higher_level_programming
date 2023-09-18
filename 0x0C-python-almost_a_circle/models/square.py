#!/usr/bin/python3
"""file contain square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, val):
        """Setter for size attribute."""
        self.width = val
        self.height = val

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the Square instance."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
