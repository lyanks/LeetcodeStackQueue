"""myfreqstack"""


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


class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.group:
            self.group[f] = Stack()
        self.group[f].push(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if self.group[self.max_freq].is_empty():
            self.max_freq -= 1
        return val
