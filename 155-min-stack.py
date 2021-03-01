from collections import deque


class MinStack:
    def __init__(self):
        self.mins = deque()
        self.stack = deque()

    def push(self, x: int) -> None:
        if not self.mins or x < self.mins[-1][0]:
            self.mins.append((x, len(self.stack)))
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if len(self.stack) <= self.mins[-1][1]:
            self.mins.pop()
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1][0]
