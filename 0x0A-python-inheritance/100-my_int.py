#!/usr/bin/python3
""" class square"""


class MyInt(int):
    def __init__(self, n) -> None:
        super().__init__()
        self.n = n

    def __eq__(self, other):
        return self.n != other

    def __ne__(self, other):
        return self.n == other
