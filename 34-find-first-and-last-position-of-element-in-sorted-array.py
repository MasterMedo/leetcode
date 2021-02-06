from bisect import bisect_left


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        i = bisect_left(nums, target)
        if i >= len(nums) or nums[i] != target:
            return [-1, -1]

        j = i+1
        while j < len(nums) and nums[j] == target:
            j += 1
        j -= 1

        return [i, j]
