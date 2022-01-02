from functools import cache


class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def ways(n):
            if n == 1:
                return 1

            return 2 * ways(n - 1) + sum(
                ways(i - 1) * ways(n - i) for i in range(2, n)
            )

        return ways(n)
