#!/usr/bin/python3
"""
Student Module
Contains student class
"""


def Student:
    """ Student class """

    def __init__(self, first_name, last_name_ age):
        """ Sets attributes for student object """
        
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dict desc of student """
        return self.__dict__
        
