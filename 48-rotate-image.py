class Solution:
    def rotate(self, m: list[list[int]]) -> None:
        n = len(m) - 1
        for r in range(len(m) // 2):
            for c in range(r, len(m) - r - 1):
                m[c][n-r], m[n-r][n-c], m[n-c][r], m[r][c] = m[r][c], m[c][n-r], m[n-r][n-c], m[n-c][r]
