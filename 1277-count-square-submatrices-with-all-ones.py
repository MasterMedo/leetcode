class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                matrix[r][c] *= min(
                    matrix[r - 1][c],
                    matrix[r][c - 1],
                    matrix[r - 1][c - 1]
                ) + 1
        return sum(map(sum, matrix))
