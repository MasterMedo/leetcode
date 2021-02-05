from collections import defaultdict


class Solution:
    def relativeSortArray(self, a: list[int], b: list[int]) -> list[int]:
        d = defaultdict(int)
        for i in a:
            d[i] += 1

        arr = []
        for i in b:
            for _ in range(d[i]):
                arr.append(i)
            del d[i]

        for i in sorted(d.keys()):
            for _ in range(d[i]):
                arr.append(i)

        return arr
