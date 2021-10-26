class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        cnt = 0
        n = nums[0]
        while i < len(nums):
            if nums[i] == n:
                if cnt >= 2:
                    del nums[i]
                    continue

                cnt += 1
            else:
                n = nums[i]
                cnt = 1

            i += 1

        return len(nums)
