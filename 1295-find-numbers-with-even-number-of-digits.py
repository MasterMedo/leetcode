class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(not len(str(n)) & 1 for n in nums)
