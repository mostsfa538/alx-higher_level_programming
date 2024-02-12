#!/usr/bin/python3
"""All"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of Square instance"""
        return "[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """return the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update values"""
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """return dictionary"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
