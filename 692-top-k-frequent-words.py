from heapq import nsmallest
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        return list(zip(*nsmallest(k, Counter(words).items(),
                                   key=lambda t: (-t[1], t[0]))))[0]
