from math import factorial as f


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return round(f(m + n - 2) / f(n - 1) / f(m - 1))
