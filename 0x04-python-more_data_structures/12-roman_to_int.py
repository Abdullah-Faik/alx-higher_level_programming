#!/usr/bin/python3
def roman_to_int(roman_string):
    rm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        sum = 0
        for i in range(len(roman_string) - 1, -1, -1):
            if roman_string[i] not in rm:
                return 0
            elif i != len(roman_string) - 1 \
                    and rm[roman_string[i]] < rm[roman_string[i + 1]]:
                sum -= rm[roman_string[i]]
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
