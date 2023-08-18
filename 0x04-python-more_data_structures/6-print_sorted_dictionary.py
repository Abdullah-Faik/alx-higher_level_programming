#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary.items())
    a.sort()
    for x in a:
        print(x[0], ": ", x[1], sep="")

