#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for st in my_string:
        if st == 'c':
            continue
        else:
            s = s + st
    return s
