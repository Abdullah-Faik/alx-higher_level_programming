#!/usr/bin/python3
"""save object as json in file"""


import json


def save_to_json_file(my_obj, filename):
    """ save object in fie as json """

    js = json.dumps(my_obj)
    with open(file=filename, mode="w", encoding="utf-8") as f:
        pyts = f.write(js)
        f.close()
    return pyts

