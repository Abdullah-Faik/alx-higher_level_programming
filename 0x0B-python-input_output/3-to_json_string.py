#!/usr/bin/python3
"""convert object to json"""


import json


def to_json_string(my_obj):
    """convert objcts to json
    Args:
        my_obj: recive obj
        jsf: recive json file
    Return: jsf file json
    """
    jsf = json.dumps(my_obj)
    return jsf
