class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [num for i in range(n) for num in (nums[i], nums[i+n])]
