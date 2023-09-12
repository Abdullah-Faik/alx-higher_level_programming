#!/usr/bin/python3
"""convert object to json"""


import json


def from_json_string(my_str):
    """convert json to obj
    Args:
        my_str: recive obj
        jsf: recive json file
    Return:  obj file jsf
    """
    jsf = json.loads(my_str)
    return jsf
