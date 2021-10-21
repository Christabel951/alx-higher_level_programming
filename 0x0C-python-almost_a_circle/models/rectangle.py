#!/usr/bin/python3
""" Module rectangle
Inherits from Base Class

"""
from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle object and inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Create a rectangle object
        Args:
            __width: width value
            __height: height value
            __x: x value
            __y: y value
            id : id

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieve width attribute value """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Retrieve the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the value of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Retrieve the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set value of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Return the area value of Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ Print Rectangle instance using char # """
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            print()
