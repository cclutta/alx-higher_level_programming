#!/usr/bin/python3
"""Student module.
Contains a Student class.
"""


class Student:
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Sets attributes for the Student object.
        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes of student. """
        for k, v in json.items():
            setattr(self, k, v)
