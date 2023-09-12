#!/usr/bin/python3
"""save object as json in file"""


import json


def load_from_json_file(filename):
    """ save object in fie as json """

    with open(file=filename, mode="r", encoding="utf-8") as f:
        my_obj = f.read()
        js = json.loads(my_obj)
        f.close()
    return js
