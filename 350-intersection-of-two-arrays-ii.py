from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d1 = defaultdict(int)
        for n in nums1:
            d1[n] += 1

        d2 = defaultdict(int)
        for n in nums2:
            d2[n] += 1

        return [n for n in d1 for _ in range(min(d1[n], d2[n]))]
