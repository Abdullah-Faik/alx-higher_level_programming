#!/usr/bin/python3
"""Node class"""

class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """__init__ method.
        Args:
            data (int): data of the node.
            next_node (Node): next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter.
        Returns:
            data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter.
        Args:
            value (int): data of the node.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node getter.
        Returns:
            next_node of the node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter.
        Args:
            value (Node): next node.
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
