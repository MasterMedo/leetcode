class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            c = min(
                a + cost[i],
                b + cost[i]
            )
            a, b = b, c
        return min(a, b)
