class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        maxLen = min(rectangles[0])
        n = 1
        for i in range(1, len(rectangles)):
            m = min(rectangles[i])

            if m == maxLen:
                n += 1
            elif m > maxLen:
                maxLen = m
                n = 1

        return n
