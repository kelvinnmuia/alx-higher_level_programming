#!/usr/bin/python3
"""creates class Node and class SinglyLinkedList"""


class Node:
    """defines class for singly linked list node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter method for data attribute"""
        return(self.__data)

    @data.setter
    def data(self, value):
        """setter method for data attribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter method for next_node attribute"""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter method for next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines singly linked list class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert new node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head
            if temp.data > new_node.data:
                new_node.next_node = temp
                self.__head = new_node
                return
            while temp.next_node is not None:
                temp2 = temp.next_node
                if temp2.data < new_node.data:
                    temp = temp2
                else:
                    new_node.next_node = temp.next_node
                    temp.next_node = new_node
                    return
            temp.next_node = new_node

    def stringrep(self):
        strrep = ""
        temp = self.__head
        while temp is not None:
            datavalue = temp.data
            strrep = strrep + str(datavalue)
            temp = temp.next_node
            if temp:
                strrep = strrep + "\n"
        return strrep

    def __repr__(self):
        return(self.stringrep())
