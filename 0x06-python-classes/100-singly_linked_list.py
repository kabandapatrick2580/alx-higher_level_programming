#!/usr/bin/python3

"""singly-linked list Classes definition."""


class Node:
    """
    Representation of a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object.

        Args:
        - data: The data to be stored in the node.
        - next_node (Node): The next node in the linked list.
                            Default is None if no next node is provided.

        Raises:
        - TypeError: If data is not  integer or next_node is not a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
        - int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Args:
        - value: The new data value.

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
        - Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Args:
        - value: The new next_node value.

        Raises:
        - TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """
    Representatio of a singly linked list.
    """

    def __init__(self):
        """
        Initialization of a SinglyLinkedList object with an empty head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (increasing order).

        Args:
        - value: The data value to be inserted.

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_sqr = self.head
            while current_sqr.next_node is not None and value >= \
                    current_sqr.next_node.data:
                current_sqr = current_sqr.next_node
            new_node.next_node = current_sqr.next_node
            current_sqr.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        - str: The string representation of the linked list.
        """
        nodes = []
        current_sqr = self.head

        while current_sqr is not None:
            nodes.append(str(current_sqr.data))
            current_sqr = current_sqr.next_node
        return "\n".join(nodes)
