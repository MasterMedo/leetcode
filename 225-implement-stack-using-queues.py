from collections import deque


class MyStack:
    def __init__(self):
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        self.queue_1.appendleft(x)

    def pop(self) -> int:
        while len(self.queue_1) > 1:
            self.queue_2.appendleft(self.queue_1.pop())

        val = self.queue_1.pop()

        while self.queue_2:
            self.queue_1.appendleft(self.queue_2.pop())

        return val

    def top(self) -> int:
        val = self.pop()
        self.push(val)
        return val

    def empty(self) -> bool:
        return len(self.queue_1) == 0 and len(self.queue_2) == 0
