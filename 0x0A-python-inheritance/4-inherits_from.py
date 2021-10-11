#!/usr/bin/python3

""" No imported module """


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a_class that inherited
    directly or indirectly from specified class, else returns False

    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
