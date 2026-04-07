""" freqstack """


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
    """ freqstack """

    def __init__(self):
        """ init """
        self._mystack = Stack()

    def push(self, val: int) -> None:
        """ push """
        if self._mystack.is_empty():
            self._mystack.push((val, 1))
        else:
            cur = self._mystack
            revers_stack = Stack()
            while True:
                v, c = self._mystack.pop()
                if v == val:
                    cnt = c + 1
                    break
                revers_stack.push((v, c))
                if self._mystack.is_empty():
                    cnt = 1
                    break
            if revers_stack.is_empty():
                self._mystack.push((val, cnt))
            fitted = False
            while not revers_stack.is_empty():
                v, c = revers_stack.pop()
                if not fitted and (cnt < c or (cnt == c and val < v)):
                    self._mystack.push((val, cnt))
                    fitted = True
                self._mystack.push((v, c))

    def pop(self) -> int:
        """ pop """
        val, cnt = self._mystack.pop()
        cnt -= 1
        if cnt > 0:
            revers_stack = Stack()
            while not self._mystack.is_empty():
                v, c = self._mystack.pop()
                if cnt >= c and v > val:
                    revers_stack.push((v, c))
                else:
                    break
            self._mystack.push((val, cnt))
            while not revers_stack.is_empty():
                self._mystack.push(revers_stack.pop())
        return val
