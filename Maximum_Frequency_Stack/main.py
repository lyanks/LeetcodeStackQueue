from collections import deque


class FreqStack:
    """freqstack"""

    def __init__(self):
        self.data = deque()

    def push(self, val: int) -> None:
        """ push """
        self.data.append(val)

    def pop(self) -> int:
        """ pop """
        freq = deque()

        def add_count(v: int) -> None:
            tmp = deque()
            found = False
            while freq:
                pair = freq.pop()
                if pair[0] == v:
                    pair[1] += 1
                    found = True
                tmp.append(pair)
            while tmp:
                freq.append(tmp.pop())
            if not found:
                freq.append([v, 1])

        def get_count(v: int) -> int:
            count = 0
            tmp: deque = deque()
            while freq:
                pair = freq.pop()
                tmp.append(pair)
                if pair[0] == v:
                    count = pair[1]
            while tmp:
                freq.append(tmp.pop())
            return count

        tmp: deque = deque()
        while self.data:
            v = self.data.pop()
            tmp.append(v)
            add_count(v)
        while tmp:
            self.data.append(tmp.pop())
        max_freq = 0
        tmp2: deque = deque()
        while freq:
            pair = freq.pop()
            tmp2.append(pair)
            if pair[1] > max_freq:
                max_freq = pair[1]
        while tmp2:
            freq.append(tmp2.pop())

        result = None
        found = False
        scratch: deque = deque()

        while self.data:
            v = self.data.pop()
            if not found and get_count(v) == max_freq:
                result = v
                found = True
            else:
                scratch.appendleft(v)

        while scratch:
            self.data.append(scratch.popleft())

        return result
