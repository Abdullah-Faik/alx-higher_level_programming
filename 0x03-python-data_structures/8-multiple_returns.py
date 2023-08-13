#!/usr/bin/python3
def multiple_returns(sentence):
    t = (0, None)
    if len(sentence) > 0:
        t = (len(sentence), sentence[0])
    return t
