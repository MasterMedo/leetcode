from functools import cache


class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        return [0, 1, 1][n] if n < 3 else self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
