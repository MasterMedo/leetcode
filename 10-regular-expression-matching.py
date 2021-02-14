from functools import cache


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        @cache
        def dp(i, j):
            if j == len(pattern):
                return i == len(string)

            matches = i < len(string) and pattern[j] in {string[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                return dp(i, j + 2) or matches and dp(i + 1, j)

            return matches and dp(i + 1, j + 1)

        return dp(0, 0)
