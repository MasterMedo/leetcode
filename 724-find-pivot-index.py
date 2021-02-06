class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = sum(nums)
        s = 0
        for i, e in enumerate(nums):
            n -= e
            if n == s:
                return i
            s += e
        return -1
