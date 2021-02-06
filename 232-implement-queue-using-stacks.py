from collections import deque


class MyQueue:
    def __init__(self):
        self._in = deque()
        self._out = deque()

    def _balance(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self._balance()
        return self._out.pop()

    def peek(self) -> int:
        self._balance()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out
