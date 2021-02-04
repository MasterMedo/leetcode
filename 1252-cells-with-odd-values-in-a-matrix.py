class Solution:
    def oddCells(self, n: int, m: int, indices: list[list[int]]) -> int:
        matrix = [[0] * m for _ in range(n)]

        for r, c in indices:
            for i in range(m):
                matrix[r][i] += 1

            for i in range(n):
                matrix[i][c] += 1

        return sum(i & 1 for row in matrix for i in row)
