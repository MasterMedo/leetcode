class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_ = not_rob = 0
        for n in nums:
            rob_, not_rob = not_rob + n, max(rob_, not_rob)

        return max(rob_, not_rob)
