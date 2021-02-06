from math import inf


class Solution:
    def findRestaurant(self, a: list[str], b: list[str]) -> list[str]:
        index = dict(zip(a, range(len(a))))
        output = []
        m = inf
        for i, e in enumerate(b):
            if e in index:
                s = index[e] + i
                if s == m:
                    output.append(e)
                elif s < m:
                    output = [e]
                    m = s
        return output
