#!/usr/bin/python3

""" No imported module """


def text_indentation(text):
    """ Print a text with 2 lines immediately after characters
     :, ? and .
    Args:
        size(int): value of size

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
