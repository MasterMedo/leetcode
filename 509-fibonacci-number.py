from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        return [0, 1][n] if n <= 1 else self.fib(n - 1) + self.fib(n - 2)
