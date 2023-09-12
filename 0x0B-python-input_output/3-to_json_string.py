#!/usr/bin/python3
import json
"""convert object to json"""


def to_json_string(my_obj):
    """convert objcts to json
    Args:
        my_obj: recive obj
    Return:
        jsf
    """
    jsf = json.dumps(my_obj)
    return jsf
