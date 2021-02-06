from math import inf


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        costs = [inf] * (len(cost) + 2)
        costs[0] = costs[1] = 0
        for i, c in enumerate(cost):
            costs[i+1] = min(costs[i + 1], costs[i] + c)
            costs[i+2] = min(costs[i + 2], costs[i] + c)

        return costs[-2]
