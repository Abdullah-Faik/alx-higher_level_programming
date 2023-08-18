#!/usr/bin/python3
def roman_to_int(roman_string):
    rm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        sum = 0
        for i in range(len(roman_string)):
            if i > 0 and rm[roman_string[i]] > rm[roman_string[i - 1]]:
                sum += rm[roman_string[i]] - 2 * rm[roman_string[i - 1]]
            else:
                sum += rm[roman_string[i]]
        return sum


# roman symbols : I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
