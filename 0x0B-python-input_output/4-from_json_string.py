#!/usr/bin/python3
""" JSON for serializing data to string representation """
import json


def from_json_string(my_str):
    """ Return the JSON representation of an object(string) """
    return json.loads(my_str)
