#!/usr/bin/python3
"""print a pascal triangle"""


def pascal_triangle(n):
    """print pascal triangle"""
    if n <= 0 or n is None:
        return []
    my = []
    my.append([1])
    for i in range(1, n):
        temp = []
        temp.append(1)
        for val in range(1, len(my[i - 1])):
            temp.append(my[i - 1][val] + my[i - 1][val - 1])
        temp.append(1)
        my.append(temp)

    return my
