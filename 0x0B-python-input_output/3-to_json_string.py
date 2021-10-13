#!/usr/bin/python3
""" JSON for serializing data to string representation """
import json


def to_json_string(my_obj):
    """ Return the JSON representation of an object(string) """
    return json.dumps(my_obj)
