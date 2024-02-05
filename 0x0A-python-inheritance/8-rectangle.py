#!/usr/bin/python3
"""inherits"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """constructor"""
        BaseGeometry.integer_validator("height", height)
        self.__height = height
        BaseGeometry.integer_validator("width", width)
        self.__width = width
