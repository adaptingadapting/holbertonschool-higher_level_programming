#!/usr/bin/python3

""" Defines a linked list "node" class """


class Node:
    """ Defines a node class with an integer and next node attribute """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list class with a head pia """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_n = Node(value)
        if not self.__head:
            self.__head = new_n
        elif self.__head.data > value:
            new_n.next_node = self.__head
            self.__head = new_n
        else:
            tmp = self.__head
            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_n.next_node = tmp.next_node
            tmp.next_node = new_n

    def __str__(self):
        l_val = []
        new_n_2 = self.__head
        while new_n_2:
            l_val.append(str(new_n_2.data))
            new_n_2 = new_n_2.next_node
        return ("\n".join(l_val))
