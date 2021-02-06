from collections import deque


class MyCircularQueue:
    def __init__(self, k: int):
        self.q = deque(maxlen=k)
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.q.popleft()
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.k
