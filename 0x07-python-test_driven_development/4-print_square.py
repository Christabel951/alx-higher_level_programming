#!/usr/bin/python3

""" No imported module """


def print_square(size):
    """ Print a square using the # character
    Args:
        size(int): value of size

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for l in range(0, size):
            for w in range(0, size):
                print("#", end="")
            print()
