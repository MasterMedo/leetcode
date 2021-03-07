class Solution:
    def restoreMatrix(self, rows: list[int], cols: list[int]) -> list[list[int]]:
        matrix = [[0] * len(cols) for _ in range(len(rows))]
        col = [0] * len(cols)
        for r, sr in enumerate(rows):
            row = 0
            for c, sc in enumerate(cols):
                matrix[r][c] = min(sc - col[c], sr - row)
                row += matrix[r][c]
                col[c] += matrix[r][c]
        return matrix
