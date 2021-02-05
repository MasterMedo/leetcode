from collections import deque


class MyCircularDeque:
    def __init__(self, k: int):
        self.q = deque(maxlen=k)
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.q:
            self.q.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.q:
            self.q.pop()
            return True
        return False

    def getFront(self) -> int:
        return self.q[0] if self.q else -1

    def getRear(self) -> int:
        return self.q[-1] if self.q else -1

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.k
