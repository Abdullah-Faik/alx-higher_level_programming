#!/usr/bin/python3
"""define a class and print it's methods"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = {}
        a = self.__dict__
        if attrs == None:
            return a
        for att in attrs:
            if att not in a:
                continue
            d[att] = a[att]
        return d
