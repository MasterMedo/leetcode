from heapq import heapify, heappush, heappop, heappushpop


class KthLargest:
    def __init__(self, k: int, arr: list[int]):
        self.heap = arr
        heapify(self.heap)
        self.k = k

        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)

        return self.heap[0]
