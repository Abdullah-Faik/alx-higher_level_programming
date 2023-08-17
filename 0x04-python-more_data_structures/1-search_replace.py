#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw = []
    for i in my_list:
        if i == search:
            nw.append(replace)
        else:
            nw.append(i)
    return nw
