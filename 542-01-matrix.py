from collections import deque


class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        visit = deque()
        seen = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visit.append((i, j))
                    seen.add((i, j))

        while visit:
            i, j = visit.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = i + di, j + dj
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and (r, c) not in seen:
                    seen.add((r, c))
                    matrix[r][c] = matrix[i][j] + 1
                    visit.append((r, c))

        return matrix
