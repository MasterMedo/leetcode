class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        arr = nums[:]
        k %= n
        for i in range(n):
            nums[i] = arr[i-k]
