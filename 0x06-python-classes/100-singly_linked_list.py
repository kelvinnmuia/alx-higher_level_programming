"""singly linked list classes"""


class Node:
    """representing a node in singly-linked list"""
    def __init__(self, data, next_node=None):
        """new node initialization

        Args:
            data (int): the new node data.
            next_node (Node)): the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get/set the nodes data"""
            return self.__data

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_nd(self):
            """Get/set the next_nd of the Node"""
            return (self.__next_node)

        @next_node.setter
        def next_nd(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value

    class SinglyLinkedList:
        """ representing the singly-linked list"""
        def __init__(self):
            """initializing the new Node in SinglyLinkedList

            node is inserted into the linked list sequentially

            Args:
                value (Node): the new node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

        def __str__(self):
            """printing the SinglyLinkedList"""
            values = []
            temp = self.__head
            while temp is not None:
                values.append(str(temp.data))
                temp = temp.next_nd
            return ('\n'.join(values))
