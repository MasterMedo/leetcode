class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        n = nums.pop()
        arr = self.subsets(nums)
        return arr + [[n] + subset for subset in arr]
