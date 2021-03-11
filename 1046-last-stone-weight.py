from heapq import heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            a, b = heappop(heap), heappop(heap)
            c = abs(a - b)
            if c > 0:
                heappush(heap, -c)

        return -heap[0] if heap else 0
