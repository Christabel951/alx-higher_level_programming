#!/usr/bin/python3

""" No imported module """
 
def add_integer(a, b=98):
    """ Adds two integer values
    Args:
        a(int): value to be added to another
        b(int): value to be added to another

    Returns:
        The sum of two integer variables
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b
