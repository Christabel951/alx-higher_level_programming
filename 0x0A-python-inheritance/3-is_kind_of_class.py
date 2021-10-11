#!/usr/bin/python3

""" No imported module """


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or of a subclass that
    inherited from a_class, else returns False

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
