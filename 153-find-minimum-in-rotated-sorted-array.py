class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while True:
            mid = lo + (hi - lo) // 2
            if nums[lo] < nums[mid] < nums[hi]:
                return nums[lo]
            elif nums[lo] > nums[mid] and nums[mid] < nums[hi]:
                hi = mid
            elif nums[lo] < nums[mid] and nums[mid] > nums[hi]:
                lo = mid
            else:
                return min(nums[lo], nums[hi])
