#!/usr/bin/python3
def uniq_add(my_list=[]):
    unq = []
    for i in my_list:
        if i not in unq:
            unq.append(i)
    return sum(unq)
