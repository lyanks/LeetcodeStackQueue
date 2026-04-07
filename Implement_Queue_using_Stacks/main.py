""" my queue """


class Stack:
    """A stack implementation."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def is_empty(self):
        """
        Check whether the stack is empty.

        :return: True if empty, False otherwise.
        """
        return len(self._items) == 0

    def push(self, item):
        """
        Add an element to the top of the stack.

        :param item: Element to add.
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top element.

        :raises IndexError: If the stack is empty.
        :return: Removed element.
        """
        if self.is_empty():
            raise IndexError("The stack is empty. Can't pop.")
        return self._items.pop()

    def peek(self):
        """
        Return the top element without removing it.

        :raises IndexError: If the stack is empty.
        :return: Top element.
        """
        if self.is_empty():
            raise IndexError("The stack is empty. Can't peek.")
        return self._items[-1]

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._items)

    def __str__(self):
        """Return string representation of the stack."""
        return "Stack: " + " -> ".join(map(str, reversed(self._items)))


class MyQueue:
    """ myqueue """

    def __init__(self):
        """ init """
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        """ push """
        self.stack_in.push(x)

    def pop(self) -> int:
        """ pop """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        """ peek """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        """ empty """
        return self.stack_out.is_empty() and self.stack_in.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
