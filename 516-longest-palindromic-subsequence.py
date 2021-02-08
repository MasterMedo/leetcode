from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def helper(lo, hi):
            if lo > hi:
                return 0
            if lo == hi:
                return 1
            if s[lo] == s[hi]:
                return 2 + helper(lo + 1, hi - 1)
            return max(helper(lo + 1, hi), helper(lo, hi - 1))

        return helper(0, len(s) - 1)
