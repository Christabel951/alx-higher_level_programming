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

    def to_json(self):
        """  retrieves a dictionary representation of a Student instance """
        return self.__dict__
