#!/usr/bin/python3
"""Base module
"""
import json
import csv


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes attributes

        Args:
            id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            n = cls(1, 1)
        else:
            n = cls(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", 'r') as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV string representation of list_objs to a file.
        """
        fields = []
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write('[]')
            else:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the CSV string representation
        """
        fields = []
        try:
            with open(cls.__name__ + ".csv", 'r') as f:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in lr.items())
                        for lr in reader]
                return [cls.create(**dct) for dct in dcts]

        except IOError:
            return []
