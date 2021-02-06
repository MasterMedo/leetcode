class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell == '1':
                    dp[r][c] = min(
                        dp[r-1][c] if r-1 >= 0 else 0,
                        dp[r][c-1] if c-1 >= 0 else 0,
                        dp[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0
                    ) + 1
                    m = max(m, dp[r][c])
        return m**2
