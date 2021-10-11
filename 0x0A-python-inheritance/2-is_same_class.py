#!/usr/bin/python3

""" No imported module """


def is_same_class(obj, a_class):
    """Returns true if obj is exactly an instance of a_class, else False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
