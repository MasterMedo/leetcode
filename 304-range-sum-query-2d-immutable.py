from collections import defaultdict


class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        sums = defaultdict(lambda: defaultdict(int))
        for r, row in enumerate(matrix):
            for c, n in enumerate(row):
                sums[r][c] = sums[r-1][c] + sums[r][c-1] - sums[r-1][c-1] + n

        self.sums = sums

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.sums[r2][c2] - self.sums[r1-1][c2] - self.sums[r2][c1-1] + self.sums[r1-1][c1-1]
