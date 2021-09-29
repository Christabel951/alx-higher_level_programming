#!/usr/bin/python3
""" No imported module """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """ Initialize class with size value using __init__ method

            Args:
                size(int): value to be assigned to a private
                            instance attribute, __size.
        """
        self.__size = size

    @property
    def size(self):
        """ Retrieve the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size value """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Reeturn the current square area """
        return self.__size ** 2
