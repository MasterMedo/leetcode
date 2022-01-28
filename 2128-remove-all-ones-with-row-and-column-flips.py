class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        reverse = [1 - grid[0][col] for col in range(len(grid[0]))]
        for row in range(1, len(grid)):
            if grid[row] != grid[0] and grid[row] != reverse:
                return False

        return True
