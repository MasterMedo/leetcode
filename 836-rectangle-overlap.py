class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x, y, w, z = rec1
        a, b, c, d = rec2
        return max(a, x) < min(c, w) and max(b, y) < min(d, z)
