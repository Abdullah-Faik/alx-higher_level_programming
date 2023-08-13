#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    x = 0
    for i in my_list:
        if x < i:
            x = i
    return x
