from functools import cache


class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])

        @cache
        def dp(k, i):
            if k == 0 and i == n:
                return 0
            if k == 0 or i == n:
                return math.inf
            ans = math.inf
            for j in range(i, n):
                cost = costs[i][j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)
