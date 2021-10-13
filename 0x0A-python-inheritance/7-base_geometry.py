#!/usr/bin/python3
""" Module 7-base_geometry
Creates a class BaseGeometry (based on 6-base_geometry.py)

"""


class BaseGeometry:
    """ Represents the base geometry object """

    def area(self):
        """
        Raises an Exception with the message
        'area() is not implemented'.

        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate the value argument
        Args:
            name(str): name of object
            value(int): argument to be validated

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
