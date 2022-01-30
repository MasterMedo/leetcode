class Solution:
    def longestLine(self, matrix: list[list[int]]) -> int:
        def add(n: int) -> None:
            nonlocal ans, line
            if n == 1:
                line += 1
                if line > ans:
                    ans = line
            else:
                line = 0

        ans = 0
        for row in matrix:  # horizontal
            line = 0
            for n in row:
                add(n)

        for col in range(len(matrix[0])):  # vertical
            line = 0
            for row in range(len(matrix)):
                n = matrix[row][col]
                add(n)

        for row in range(len(matrix)):  # diagonal right bottom
            line = 0
            i = 0
            while row + i < len(matrix) and i < len(matrix[0]):
                n = matrix[row + i][i]
                add(n)
                i += 1

        for col in range(1, len(matrix[0])):  # diagonal right top
            line = 0
            i = 0
            while i < len(matrix) and col + i < len(matrix[0]):
                n = matrix[i][col + i]
                add(n)
                i += 1

        for row in range(len(matrix)):  # diagonal left top
            line = 0
            r = c = 0
            while row + r >= 0 and c < len(matrix[0]):
                n = matrix[row + r][c]
                add(n)
                r -= 1
                c += 1

        for col in range(1, len(matrix[0])):  # diagonal left bottom
            line = 0
            c = 0
            r = len(matrix) - 1
            while r >= 0 and col + c < len(matrix[0]):
                n = matrix[r][col + c]
                add(n)
                r -= 1
                c += 1

        return ans
