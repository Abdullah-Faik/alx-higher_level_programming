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

class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """__init__ method.
        """
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert method.
        Args:
            value (int): data of the node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """__str__ method.
        Returns:
            string representation of the list.
        """
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]
