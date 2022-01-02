class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        for row in range(m):
            for col in range(n):
                grid[row][col] = -grid[row][col]
            grid[row].insert(0, 0)

        grid.insert(0, [0] * len(grid[0]))

        grid[0][1] = 1

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == -1:
                    continue

                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                if grid[i-1][j] == -1:
                    grid[i][j] += 1

                if grid[i][j-1] == -1:
                    grid[i][j] += 1

        return grid[-1][-1]
