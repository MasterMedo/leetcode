class Solution:
    def jump(self, nums: List[int]) -> int:
        prev_max_jump = 0
        max_jump = nums[0]
        jumps = 0
        for i in range(1, len(nums)):
            if i > prev_max_jump:
                jumps += 1
                prev_max_jump = max_jump

            if i + nums[i] > max_jump:
                max_jump = i + nums[i]

        return jumps
