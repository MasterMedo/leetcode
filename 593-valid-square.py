from collections import defaultdict


class Solution:
    def validSquare(self, *points) -> bool:
        e = 10**(-6)

        sides = defaultdict(int)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = round(abs(complex(x1, y1) - complex(x2, y2)), 12)
                sides[d] += 1

        if len(sides) == 2:
            a, d = sorted(sides)
            if abs(a * pow(2, 0.5) - d) < e and sides[a] == 4 and sides[d] == 2:
                return True

        return False
