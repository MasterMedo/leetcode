class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            elif zeros:
                nums[i - zeros] = n

        for i in range(zeros):
            nums[-i - 1] = 0
