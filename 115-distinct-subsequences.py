from functools import cache
from bisect import bisect_left

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def numInTable(i_t: int, i_s: int) -> int:
            print(i_t, i_s)
            if i_t == 0:
                return 1

            i_lowest = bisect_left(arr[i_t], i_s)
            return sum(numInTable(i_t - 1, arr[i_t][n]) for n in range(i_lowest))

        arr = [[-1]]
        for i_t, char_t in enumerate(t):
            arr.append([])
            if not arr[-2]:
                return 0
            for i_s in range(arr[-2][0] + 1, len(s)):
                if s[i_s] == char_t:
                    arr[-1].append(i_s)
        if not arr[-1]:
            return 0
        return numInTable(len(arr) - 1, arr[-1][-1] + 1)
