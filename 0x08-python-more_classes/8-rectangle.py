#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """A Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """constructor

        Args:
            width (int): the width
            height (int): the height
        """

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__height = height

        Rectangle.number_of_instances += 1

    def __del__(self):
        """The Death"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
            value (int): width value
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height

        Args:
            value (int): height value
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def print(self):
        """prints rectangle"""
        len_wdith = self.__width
        len_height = self.__height
        ans = ""

        if len_wdith == 0 or len_height == 0:
            return ans

        for i in range(len_height):
            for j in range(len_wdith):
                ans += str(self.print_symbol)
            if i != len_height - 1:
                ans += '\n'
        return ans

    def __str__(self):
        """returns string of rectangle"""
        return self.print()

    def __repr__(self):
        """return rectangle information"""
        len_wdith = self.__width
        len_height = self.__height

        return "Rectangle({}, {})".format(len_wdith, len_height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """who is bigger"""
        if type(rect_1) is not Rectangle:
            raise TabError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TabError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
