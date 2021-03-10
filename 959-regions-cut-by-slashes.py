from collections import deque


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        seen = {(i, j, k) for i in range(len(grid))
                for j in range(len(grid[0])) for k in range(4)}

        count = 0
        while seen:
            count += 1
            visit = deque([seen.pop()])
            while visit:
                i, j, k = visit.popleft()
                c = grid[i][j]
                neighbours = []
                if c == ' ' or (c == '/' and k in (0, 2)) or (c == '\\' and k in (1, 2)):
                    neighbours.append((i, j - 1, 3))
                    if (i, j, 2) in seen:
                        seen.remove((i, j, 2))
                if c == ' ' or (c == '/' and k in (0, 2)) or (c == '\\' and k in (0, 3)):
                    neighbours.append((i - 1, j, 1))
                    if (i, j, 0) in seen:
                        seen.remove((i, j, 0))
                if c == ' ' or (c == '/' and k in (1, 3)) or (c == '\\' and k in (1, 2)):
                    neighbours.append((i + 1, j, 0))
                    if (i, j, 1) in seen:
                        seen.remove((i, j, 1))
                if c == ' ' or (c == '/' and k in (1, 3)) or (c == '\\' and k in (0, 3)):
                    neighbours.append((i, j + 1, 2))
                    if (i, j, 3) in seen:
                        seen.remove((i, j, 3))

                for i, j, k in neighbours:
                    if (i, j, k) in seen:
                        seen.remove((i, j, k))
                        visit.append((i, j, k))

        return count
