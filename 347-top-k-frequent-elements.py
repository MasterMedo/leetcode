from collections import Counter
from heapq import nlargest


class Solution:
    def topKFrequent(self, arr: list[int], k: int) -> list[int]:
        if k == len(arr):
            return arr

        count = Counter(arr)
        return nlargest(k, count.keys(), key=count.get)
