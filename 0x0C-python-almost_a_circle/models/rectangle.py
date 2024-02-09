#!/usr/bin/python3
"""All"""
from models.base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return Private attribute for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set Private attribute for width"""
        self.__width = value

    @property
    def height(self):
        """Return Private attribute for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set Private attribute for height"""
        self.__height = value

    @property
    def x(self):
        """Return Private attribute for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set Private attribute for x"""
        self.__x = value

    @property
    def y(self):
        """Return Private attribute for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set Private attribute for y"""
        self.__y = value
