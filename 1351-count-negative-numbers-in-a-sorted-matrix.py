class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        return sum(cell < 0 for row in grid for cell in row)
