#!/usr/bin/python3


""" No imported module(s) """


class Rectangle:
    """ Represent a rectangle. """

    def __init__(self, width=0, height=0):
        """ Initialize Rectangle.

        Args:
            width(int): Breadth measurement.
            height(int): Peak measurement.

        """

        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Print a Rectangular object using the # character, width and
        height measurements

        """
        rec_str = ""
        if self.__width == 0 or self.__height == 0:
            return rec_str
        else:
            for h in range(0, self.__height):
                for w in range(0, self.__width):
                    rec_str += "#"
                rec_str += "\n"
            return rec_str[:-1]

    @property
    def width(self):
        """ Retrieve width value. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set/define the value of width.

        Args:
            value(int): value to be assigned to private attribute.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve the value of height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set/ define the value of height.

        Args:
            value(int): value to be assigned to private attribute height.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Calculate the area of a rectangle

        Returns:
            The rectangle's area

        """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the primeter of a rectangle ""

        Returns:
            The rectangle's perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
