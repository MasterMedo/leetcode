from collections import Counter


class Solution:
    def majorityElement(self, arr: list[int]) -> list[int]:
        return [c for c, n in Counter(arr).most_common(3) if n > len(arr) / 3]
