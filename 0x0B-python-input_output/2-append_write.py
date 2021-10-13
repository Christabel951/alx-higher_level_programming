#!/usr/bin/python3
""" Module - append_write """


def append_write(filename="", text=""):
    """ append a string at the end of a text file and return char num """
    with open(filename, 'a+') as f:
        return f.write(text)
