from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(c * n for c, n in sorted(Counter(s).items(),
                                                key=lambda x: (-x[1], x[0])))
