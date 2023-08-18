#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    for key in list(a_dictionary.keys()):
        if key == key:
            del a_dictionary[key]
    return a_dictionary
