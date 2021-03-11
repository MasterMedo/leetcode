from functools import cache


class Solution:
    def isInterleave(self, a: str, b: str, c: str) -> bool:
        @cache
        def dfs(i: int, j: int, k: int) -> bool:
            if i >= len(a) and j >= len(b) and k >= len(c):
                return True

            if k >= len(c):
                return False

            if i < len(a) and a[i] == c[k]:
                if dfs(i + 1, j, k + 1):
                    return True

            if j < len(b) and b[j] == c[k]:
                if dfs(i, j + 1, k + 1):
                    return True

            return False

        return dfs(0, 0, 0)
