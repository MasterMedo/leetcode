class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if r == c == 0:
                    continue

                grid[r][c] = min(
                    grid[r - 1][c] if r - 1 >= 0 else float('inf'),
                    grid[r][c - 1] if c - 1 >= 0 else float('inf')
                ) + cell

        return grid[-1][-1]
