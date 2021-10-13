#!/usr/bin/python3
""" Module 100-my_int
Creates a class MyInt that inherits from int.

"""


class MyInt(int):
    """ Represents an int object, Reverse == and != """

    def __eq__(self, other):
        """ Invert == to != """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Invert != to =="""
        return super().__eq__(other)
