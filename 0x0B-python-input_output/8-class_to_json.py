#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:

"""


def class_to_json(obj):
    """
    Create a dictionary description of obj
    Args:
        obj(object): object to be serialized
    Returns:
        Dictionary description of obj
    """
    return obj.__dict__
