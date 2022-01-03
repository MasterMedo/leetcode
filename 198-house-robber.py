class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = not_rob = 0
        for n in nums:
            rob, not_rob = not_rob + n, max(rob, not_rob)

        return max(rob, not_rob)
