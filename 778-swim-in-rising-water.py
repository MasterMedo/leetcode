from collections import deque
from bisect import bisect_left


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        seen = [[False] * N for _ in range(N)]
        seen[0][0] = True
        t = 0
        front = deque([(0, 0)])
        values = sorted([n for row in grid for n in row])
        i = bisect_left(values, max(grid[0][0], grid[-1][-1]))
        for t in values[i:]:
            next_front = deque()
            while front:
                r, c = front.pop()
                if t >= grid[r][c]:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and not seen[nr][nc] and t >= grid[nr][nc]:
                            if nr == nc == N - 1:
                                return t

                            seen[nr][nc] = True
                            front.append((nr, nc))

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and not seen[nr][nc]:
                        next_front.append((r, c))
                        break

            front = next_front
