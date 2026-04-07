"""Linked Queue implementation using a singly linked list."""


class Node:
    """A node in a singly linked list used by the queue."""

    def __init__(self, value, next_node=None):
        """
        Initialize a node.

        :param value: The value stored in the node.
        :param next_node: Reference to the next node (default is None).
        """
        self.value = value
        self.next = next_node

    def __repr__(self):
        """Return string representation of the node."""
        return str(self.value)

    def __eq__(self, other):
        """Compare nodes by value."""
        if not isinstance(other, Node):
            return False
        return self.value == other.value


class LinkedQueue:
    """A FIFO queue implemented using a linked list."""

    def __init__(self):
        """Initialize an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        """
        Check whether the queue is empty.

        :return: True if empty, False otherwise.
        """
        return self._size == 0

    def add(self, item):
        """
        Add an element to the end of the queue.

        :param item: Element to add.
        """
        new_node = Node(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def pop(self):
        """
        Remove and return the front element of the queue.

        :raises IndexError: If the queue is empty.
        :return: Value of removed element.
        """
        if self.is_empty():
            raise IndexError("The queue is empty. Can't pop.")
        value = self._head
        self._head = self._head.next
        self._size -= 1
        if self._head is None:
            self._tail = None

        return value

    def peek(self):
        """
        Return the front element without removing it.

        :raises IndexError: If the queue is empty.
        :return: Value at the front.
        """
        if self.is_empty():
            raise IndexError("The queue is empty. Can't peek.")
        return self._head

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def __str__(self):
        """Return string representation of the queue."""
        values = []
        current = self._head
        while current:
            values.append(str(current.value))
            current = current.next
        return "Queue: " + " <- ".join(values)
