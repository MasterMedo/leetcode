class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = 0
        count = 0
        for n in nums:
            if count == 0:
                majority = n
            if n == majority:
                count += 1
            else:
                count -= 1
        return majority
