#!/usr/bin/python3
"""define a class and print it's methods"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dicr = {}
        a = self.__dict__
        if attrs is None:
            return a

        for att in attrs:
            if att not in a:
                continue
            dicr[att] = a[att]
        return dicr

    def reload_from_json(self, json):
        for key in json.keys():
            self.__dict__[key] = json[key]
        
