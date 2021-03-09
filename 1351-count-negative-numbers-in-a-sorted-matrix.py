class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        return sum(len(row) - next((i for i in range(len(row)) if row[i] < 0), len(row))
                   for row in grid)
