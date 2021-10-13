#!/usr/bin/python3
"""
Module 100-append_after.
Inserts a line of text to a file,after each line containing a specific str.

"""


def append_after(filename="", search_string="", new_string=""):
    """ Appends the new_string after a match with the search_string """
    with open(filename, 'r+') as f:
        txt = f.readlines()
        i = 0
        for line in txt:
            if line.find(search_string) is not -1:
                txt.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(txt))
