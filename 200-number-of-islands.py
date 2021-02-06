from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def sink(x, y):
            grid[x][y] = 0
            visit = deque([(x, y)])
            while visit:
                x, y = visit.popleft()
                for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                    z, w = x + dx, y + dy
                    if 0 <= z < len(grid) and 0 <= w < len(grid[0]) and grid[z][w] == '1':
                        grid[z][w] = '0'
                        visit.append((z, w))

        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    islands += 1
                    sink(x, y)

        return islands
