from heapq import heappush, heappushpop


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        ratios = [wage[i] / quality[i] for i in range(len(wage))]
        workers = sorted(range(len(wage)), key=lambda i: (ratios[i], quality[i], wage[i]))
        cost = None
        total = 0
        heap = []
        for i in workers:
            total += quality[i]
            if len(heap) >= k:
                total += heappushpop(heap, -quality[i])
                cost = min(cost, ratios[i] * total)
            else:
                heappush(heap, -quality[i])
                if len(heap) >= k:
                    cost = ratios[i] * total
        return cost
