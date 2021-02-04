class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        distance = 0
        x, y = points.pop()
        for z, w in reversed(points):
            distance += max(abs(x - z), abs(y - w))
            x, y = z, w

        return distance
