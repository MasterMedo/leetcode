from functools import cache


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        @cache
        def dp(i, j):
            if j >= len(pattern):
                return i >= len(string)

            if pattern[j] == '*':
                return dp(i, j + 1) or i < len(string) and dp(i + 1, j)

            return i < len(string) and pattern[j] in ('?', string[i]) and dp(i + 1, j + 1)

        return dp(0, 0)
