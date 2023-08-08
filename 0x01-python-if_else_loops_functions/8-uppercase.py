#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        x = str[i]
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            x = chr(ord(str[i]) - 32)
        print("{}".format(x), end="")
    print("")
