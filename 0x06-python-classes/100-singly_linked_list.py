#!/usr/bin/python3
"""This is singly_linked_list module."""


class Node:
    """A class that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initialization method"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        """initialization method"""
        self.__head = None

    def sorted_insert(self, value):
        """method that inserts a new Node into sorted position in the list"""
        new = Node(value)
        tmp = self.__head
        add_start = False

        if not self.__head:
            self.__head = new
            new.next_node = None
        else:
            if value < self.__head.data:
                add_start = True
            while tmp.next_node and value > tmp.next_node.data\
                    and not add_start:
                tmp = tmp.next_node
            if not add_start:
                new.next_node = tmp.next_node
                tmp.next_node = new
            else:
                new.next_node = tmp
                self.__head = new
            new.data = value

    def __str__(self):
        s = ""
        curr = self.__head

        while curr:
            s += str(curr.data) + '\n'
            curr = curr.next_node
        return s[: -1]
