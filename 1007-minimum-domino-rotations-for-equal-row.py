from math import inf


class Solution:
    def minDominoRotations(self, a: list[int], b: list[int]) -> int:
        def flipper(x):
            up = down = 0
            for i, j in zip(a, b):
                if x == i:
                    if x != j:
                        down += 1
                else:
                    if x == j:
                        up += 1
                    else:
                        return inf

            return min(up, down)

        m = min(flipper(a[0]), flipper(b[0]))
        return m if m != inf else -1
