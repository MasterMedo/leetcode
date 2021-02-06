class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiral = []
        d = 1
        xy = 0
        y = len(matrix)
        x = len(matrix[0])
        spiral.append(matrix[0][0])
        while x > 0 and y > 0:
            for _ in range(x-1):
                xy += d
                spiral.append(matrix[int(xy.imag)][int(xy.real)])

            d *= 1j
            for _ in range(y-1):
                xy += d
                spiral.append(matrix[int(xy.imag)][int(xy.real)])

            if y == 1 or x == 1:
                break

            d *= 1j
            for _ in range(x-1):
                xy += d
                spiral.append(matrix[int(xy.imag)][int(xy.real)])

            d *= 1j
            for _ in range(y-2):
                xy += d
                spiral.append(matrix[int(xy.imag)][int(xy.real)])

            d *= 1j
            xy += d

            if len(spiral) < len(matrix)*len(matrix[0]):
                spiral.append(matrix[int(xy.imag)][int(xy.real)])

            x -= 2
            y -= 2
        return spiral
