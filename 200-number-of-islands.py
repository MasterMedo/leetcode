from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    islands += 1
                    visit = deque([(r, c)])
                    while visit:
                        x, y = visit.pop()
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                visit.append((nx, ny))
        return islands
