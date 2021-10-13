#!/usr/bin/python3
""" JSON for serializing data to string representation """
import json


def save_to_json_file(my_obj, filename):
    """Return the JSON representation of an object(string) to txt file"""
    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
