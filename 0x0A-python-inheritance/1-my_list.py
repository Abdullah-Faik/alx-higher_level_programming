#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """ class the print sorted list"""

    def print_sorted(self):
        """
        print sorted list

        Args:
            only self
        Return:
            None
        """
        list_1 = self.copy()
        list_1.sort()
        print(list_1)
