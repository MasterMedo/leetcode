from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        islands = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 0:
                    closed = True
                    visit = deque([(r, c)])
                    while visit:
                        r0, c0 = visit.popleft()
                        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            r1 = r0 + x
                            c1 = c0 + y
                            if 0 <= r1 < len(grid) and 0 <= c1 < len(row):
                                if grid[r1][c1] == 0:
                                    grid[r1][c1] = 2
                                    visit.append((r1, c1))
                            else:
                                closed = False
                    islands += closed
        return islands
