#!/usr/bin/python3
""" This module prints text with 2 new lines after each of these characters: .
    ? and :
"""


def text_indentation(text):
    """ This function prints text with 2 new lines after each of these
        characters: . ? and :
    Args:
        text (str): text to print
    Returns:
        None
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in ".?:":
            continue
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
