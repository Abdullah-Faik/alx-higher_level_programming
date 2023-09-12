#!/usr/bin/python3
"""save args as json file"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []

obj.extend(sys.argv[1:])
save_to_json_file(obj, "add_item.json")
