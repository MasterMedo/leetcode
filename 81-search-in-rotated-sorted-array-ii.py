class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        lo = 0
        hi = len(nums) - 1
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True

        right = True
        if nums[mid] < target:
            if nums[hi] < target and nums[hi] > nums[mid]:
                right = False

        left = True
        if nums[mid] > target:
            if nums[lo] > target and nums[lo] < nums[mid]:
                left = False

        if right:
            right = self.search(nums[mid + 1 :], target)

        if left:
            left = self.search(nums[:mid], target)

        return left or right
