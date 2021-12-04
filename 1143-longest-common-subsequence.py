class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        grid = [[0]*(len(b) + 1) for _ in range(len(a) + 1)]
        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                grid[i][j] = max(
                    grid[i-1][j],
                    grid[i][j-1],
                    grid[i-1][j-1] + (a[i - 1] == b[j - 1])
                )

        return grid[-1][-1]
