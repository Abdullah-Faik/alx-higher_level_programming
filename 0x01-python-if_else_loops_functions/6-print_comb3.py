#!/usr/bin/python3
for i in range(10):
    j = i + 1
    for j in range(j, 10):
        if i != 8:
            print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:d}{:d}".format(i, j))
