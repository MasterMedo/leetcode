class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]

        matrix = [[0] * n for _ in range(n)]
        i = 1
        xy = 0
        d = 1j
        while matrix[int(xy.real)][int(xy.imag)] == 0:
            matrix[int(xy.real)][int(xy.imag)] = i
            i += 1
            zw = xy + d
            if zw.real < len(matrix) and zw.imag < len(matrix[0]) and matrix[int(zw.real)][int(zw.imag)] == 0:
                xy = zw
            else:
                d /= 1j
                xy += d

        return matrix
