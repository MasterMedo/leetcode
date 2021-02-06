class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r - x > 0.5:
            r = (r + x/r) / 2
        return int(r)
