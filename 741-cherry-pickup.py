from functools import cache


class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        @cache
        def f(a, b, c, d):
            if a > c:
                return f(c, d, a, b)

            if len(grid) in (a, b, c, d):
                return -1

            if grid[a][b] == -1 or grid[c][d] == -1:
                return -1

            if {a, b, c, d} == {len(grid) - 1}:
                return grid[-1][-1]

            dd = f(a + 1, b, c + 1, d)
            dr = f(a + 1, b, c, d + 1)
            rd = f(a, b + 1, c + 1, d)
            rr = f(a, b + 1, c, d + 1)

            m = max(dd, dr, rd, rr)
            if m == -1:
                return -1

            if a == c and b == d:
                return m + grid[a][b]

            return m + grid[a][b] + grid[c][d]

        return max(f(0, 0, 0, 0), 0)
