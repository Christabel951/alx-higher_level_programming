#!/usr/bin/python3
""" Module 10-square
Creates a class Square that inherits from Rectangle (9-rectangle.py).

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a square object """

    def __init__(self, size):
        """ Initializes an object of type Square """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns a formatted string."""
        return str("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """ Calculate area of Rectangle object """
        return self.__size * self.__size