#!/usr/bin/python3
""" Module 9-student"""


class Student:
    """
    Represents a student
    Public Attributes:
                first_name
                last_name
                age
    Public method:
                to_json()
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes a student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary representation of a Student instance """
        this_dict = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    this_dict.update({i: self.__dict__[i]})
            return this_dict
        return self.__dict__.copy()
