from heapq import heapify, heappush, heappop


class Solution:
    def trapRainWater(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        water = [row.copy() for row in heights]
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                water[r][c] = None

        visit = [(water[r][c], r, c) for a in range(rows)
                 for r, c in ((a, 0), (a, cols - 1))] +\
                [(water[r][c], r, c) for a in range(cols)
                 for r, c in ((0, a), (rows - 1, a))]
        heapify(visit)
        seen = set()
        while visit:
            _, r, c = heappop(visit)
            for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                nr, nc = r + dr, c + dc
                if 0 < nr < rows - 1 and 0 < nc < cols - 1 and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    if water[nr][nc] is None:
                        water[nr][nc] = max(heights[nr][nc], water[r][c])

                    elif heights[nr][nc] <= water[r][c]:
                        if water[nr][nc] > water[r][c]:
                            water[nr][nc] = water[r][c]

                    elif heights[nr][nc] < water[nr][nc]:
                        water[nr][nc] = heights[nr][nc]

                    heappush(visit, (water[nr][nc], nr, nc))

        return sum(water[r][c] - heights[r][c]
                   for r in range(rows) for c in range(cols))
