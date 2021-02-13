class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if r > 0 and c > 0 and cell != matrix[r - 1][c - 1]:
                    return False
        return True
