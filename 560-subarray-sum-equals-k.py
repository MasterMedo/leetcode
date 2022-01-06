from collections import defaultdict
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int, {0: 1})
        ans = 0
        for s in accumulate(nums):
            ans += counts[s - k]
            counts[s] += 1
        return ans
