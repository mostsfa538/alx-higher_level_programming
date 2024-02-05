#!/usr/bin/python3
"""a Class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """vaildator"""
        if type(self.name) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        elif self.name <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
