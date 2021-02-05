class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        pascal = [[1], [1, 1]]
        for _ in range(numRows - 2):
            pascal.append([1] + [pascal[-1][i] + pascal[-1][i+1]
                                 for i in range(len(pascal[-1]) - 1)] + [1])

        return pascal
