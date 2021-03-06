#!/usr/bin/python3
""" No imported module """


class Square:
    """ Represent a square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize class with size value using __init__ method

            Args:
                size(int): value to be assigned to a private
                            instance attribute, __size.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Retrieve the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the position value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Reeturn the current square area """
        return self.__size ** 2

    def my_print(self):
        """ Print in stdout the square with the character # at position """
        if self.__size == 0:
            print()
        else:
            for k in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for l in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
