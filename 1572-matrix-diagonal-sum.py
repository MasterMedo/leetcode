class Solution:
    def diagonalSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        s = 0
        for i in range(n):
            s += matrix[i][i]
            if n - i - 1 != i:
                s += matrix[n - i - 1][i]

        return s
