class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        def bfs(r, c, current, grid):
            profit = current
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] > 0:
                    matrix = [row.copy() for row in grid]
                    matrix[nr][nc] = 0
                    profit = max(profit, bfs(nr, nc, current + grid[nr][nc], matrix))

            return profit

        profit = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    matrix = [row.copy() for row in grid]
                    matrix[r][c] = 0
                    profit = max(profit, bfs(r, c, grid[r][c], matrix))

        return profit
