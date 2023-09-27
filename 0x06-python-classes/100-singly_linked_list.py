"""singly linked list classes"""


class Node:
    """representing a node in singly-linked list"""
    def __init__(self, data, next_nd=None):
        """new node initialization

        Args:
            data (int): the new node data.
            next_nd (Node)): the next node in the linked list
        """
        self.data = data
        self.next_nd = next_nd

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
                raise TypeError("next_nd must be a Node object")
            self.__next_nd = value

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
            new.next_nd = None
            self.__head = new
        elif self.__head.data > value:
            new.next_nd = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_nd is not None and
                    temp.next_nd.data < value):
                temp = temp.next_nd
            new.next_nd = temp.next_nd
            temp.next_nd = new

        def __str__(self):
            """printing the SinglyLinkedList"""
            values = []
            temp = self.__head
            while temp is not None:
                values.append(str(temp.data))
                temp = temp.next_nd
            return ('\n'.join(values))
