#!/usr/bin/python3
"""define a class and print it's methods"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        d = {}
        a = self.__dict__
        for att in attrs:
            d[att] = a[att]
        return d
