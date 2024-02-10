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
        return self.size

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value
