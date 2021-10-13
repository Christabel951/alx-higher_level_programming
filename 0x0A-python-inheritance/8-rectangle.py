#!/usr/bin/python3
""" Module 8-rectangle
Creates a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a Rectangle object """

    def __init__(self, width, height):
        """ Initializes an object of type Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
