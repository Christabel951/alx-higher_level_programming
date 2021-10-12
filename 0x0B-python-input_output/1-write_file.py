#!/usr/bin/python3
""" Module - write_file """


def write_file(filename="", text=""):
    """ Writes a string to a text file and return char nun """
    with open(filename, 'w+') as f:
        return f.write(text)
