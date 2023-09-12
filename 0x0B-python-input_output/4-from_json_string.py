#!/usr/bin/python3
"""convert object to json"""


import json


def from_json_string(my_str):
    jsf = json.loads(my_str)
    return jsf
