class Solution:
    def intervalIntersection(self, a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        intersections = []
        i = j = 0
        while i < len(a) and j < len(b):
            start = max(a[i][0], b[j][0])
            end = min(a[i][1], b[j][1])
            if start <= end:
                intersections.append([start, end])
            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1

        return intersections
