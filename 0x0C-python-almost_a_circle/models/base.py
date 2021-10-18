#!/usr/bin/python3
""" Module base
Manages the id attribute in all future classes and help eliminate
unnecessary code duplicationvoid duplicating the same code.

"""


class Base:
    """ Represents the base for all other classes in modules project
    Attributes:
            __nb_object(int): incremented when the id value is None

            __init__: class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
