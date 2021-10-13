#!/usr/bin/python3
""" JSON for serializing data to string representation """
import json


def load_from_json_file(filename):
    """Return the JSON representation of an object from str"""
    with open(filename, 'r') as f:
        return json.load(f)
