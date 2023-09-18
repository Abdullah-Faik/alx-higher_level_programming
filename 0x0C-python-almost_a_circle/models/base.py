#!/usr/bin/python3
"""clss base for project"""

import json


class Base:
    """basic class for python"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        self.id = None
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def reset():
        """reset nb_objects"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        if list_objs is None:
            list_objs = []
        list_objs = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """load from file"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the class and update its attributes from the dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None

        dummy.update(**dictionary)
        return dummy
