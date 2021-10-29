class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n * (n + 1)) // 2
        for n in nums:
            s -= n

        return s
