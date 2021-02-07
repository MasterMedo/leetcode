from collections import defaultdict
from math import inf, gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        max_ = 0
        for x1, y1 in points:
            slopes = defaultdict(int)
            duplicates = 0
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                else:
                    dy, dx = y2 - y1, x2 - x1
                    d = gcd(dy, dx)
                    slope = (dy/d, dx/d) if dx else (inf,)
                    slopes[slope] += 1

            points_on_line = max(slopes.values()) if slopes.values() else 0
            max_ = max(points_on_line + duplicates, max_)

        return max_
