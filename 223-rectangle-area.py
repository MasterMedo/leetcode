class Solution:
    def computeArea(self, x0a: int, y0a: int, x1a: int, y1a: int, x0b: int, y0b: int, x1b: int, y1b: int) -> int:
        a = (x1a - x0a) * (y1a - y0a)
        b = (x1b - x0b) * (y1b - y0b)

        x0c = max(x0a, x0b)
        x1c = min(x1a, x1b)
        y0c = max(y0a, y0b)
        y1c = min(y1a, y1b)
        if x1c < x0c or y1c < y0c:
            return a + b

        c = (x1c - x0c) * (y1c - y0c)
        return a + b - c
