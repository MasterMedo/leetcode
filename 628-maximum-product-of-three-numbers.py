from math import inf


class Solution:
    def maximumProduct(self, arr: list[int]) -> int:
        hi1 = hi2 = hi3 = -inf
        lo1 = lo2 = inf
        for n in arr:
            if n >= hi1:
                hi3, hi2, hi1 = hi2, hi1, n
            elif n >= hi2:
                hi3, hi2 = hi2, n
            elif n > hi3:
                hi3 = n
            if n <= lo1:
                lo2, lo1 = lo1, n
            elif n < lo2:
                lo2 = n

        return max(hi1 * hi2 * hi3, lo1 * lo2 * hi1)
