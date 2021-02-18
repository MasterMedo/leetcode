from heapq import heappush, heappop, heappushpop


class Solution:
    def minDifference(self, arr: list[int]) -> int:
        if len(arr) <= 4:
            return 0

        minHeap = []
        maxHeap = []
        for n in arr:
            if len(minHeap) >= 4:
                heappushpop(minHeap, -n)
                heappushpop(maxHeap, n)
            else:
                heappush(minHeap, -n)
                heappush(maxHeap, n)

        mins = [-heappop(minHeap) for _ in range(4)]
        maxs = [heappop(maxHeap) for _ in range(4)]
        return max(min(maxs[3 - i] - mins[i] for i in range(4)), 0)
