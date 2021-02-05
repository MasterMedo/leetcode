class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        grid = [[0]*len(b) for _ in range(len(a))]
        for i, c1 in enumerate(a):
            for j, c2 in enumerate(b):
                left = grid[i-1][j] if i != 0 else 0
                up = grid[i][j-1] if j != 0 else 0
                diag = grid[i-1][j-1] if i != 0 and j != 0 else 0
                grid[i][j] = max(left, up, diag + (c1 == c2))

        return grid[-1][-1]
