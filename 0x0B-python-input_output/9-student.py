#!/usr/bin/python3
"""Student Module
Contains student class
"""


def Student:
    """class Student that defines a student by. """

    def __init__(self, first_name, last_name, age):
        """Initialize new student

        Args:
            first_name: first name of student
            last_name : last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict desc of student """
        return self.__dict__
