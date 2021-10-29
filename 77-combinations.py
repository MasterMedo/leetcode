from functools import cache


class Solution:
    @cache
    def combine(self, n: int, k: int, d: int = 0) -> List[List[int]]:
        if k <= 0:
            return [[]]

        result = []
        for i in range(d + 1, n + 2 - k):
            arr = self.combine(n, k - 1, i)
            for comb in arr:
                result.append([i, *comb])

        return result
