class Solution:
    def findLength(self, a: list[int], b: list[int]) -> int:
        table = [[0] * len(b) for _ in range(len(a))]
        m = 0
        for r, char1 in enumerate(a):
            for c, char2 in enumerate(b):
                last = 0 if r == 0 or c == 0 else table[r-1][c-1]
                table[r][c] = 0 if char1 != char2 else last + 1
                m = max(m, table[r][c])
        return m
