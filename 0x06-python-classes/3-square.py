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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Reeturn the current square area """
        return self.__size ** 2
