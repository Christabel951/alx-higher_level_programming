#!/usr/bin/python3

""" Module 1-my_list
Creates MyList class which inherits from the list class

"""


class MyList(list):
    """ Class MyList inherits from list - subclass """

    def print_sorted(self):
        """ Prints list items sorted in ascending order """
        print(sorted(self))
