#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ls = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else :
        for i in range(len(my_list)):
            if i == idx :
                ls.append(element)
            else:
                ls.append(my_list[i])
    return ls
