#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw = []
    for m in matrix:
        tmp = []
        for val in m:
            tmp.append(val**2)
        nw.append(tmp)
    return nw
