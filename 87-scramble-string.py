from functools import cache


class Solution:
    def isScramble(self, a: str, b: str) -> bool:
        @cache
        def dp(lo_a, hi_a, lo_b, hi_b):
            if lo_a == hi_a:
                return a[lo_a] == b[lo_b]

            for i in range(lo_a + 1, hi_a + 1):
                if (
                    dp(lo_a, i - 1, lo_b, lo_b + i - lo_a - 1)
                    and dp(i, hi_a, lo_b + i - lo_a, hi_b)
                ) or (
                    dp(i, hi_a, lo_b, lo_b + hi_a - i)
                    and dp(lo_a, i - 1, lo_b + hi_a - i + 1, hi_b)
                ):
                    return True
            return False

        return dp(0, len(a) - 1, 0, len(b) - 1)
