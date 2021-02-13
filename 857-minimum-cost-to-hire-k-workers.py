from heapq import heappush, heappop
from math import inf


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], K: int) -> float:
        ratios = [wage[i] / quality[i] for i in range(len(wage))]
        workers = sorted(range(len(wage)), key=lambda i: (ratios[i], quality[i], wage[i]))
        cost = inf
        total = 0
        heap = []
        for i in workers:
            heappush(heap, -quality[i])
            total += quality[i]

            if len(heap) > K:
                total += heappop(heap)

            if len(heap) == K:
                cost = min(cost, ratios[i] * total)

        return cost
