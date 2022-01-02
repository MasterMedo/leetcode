class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for lowest in nums:
            if lowest - 1 not in nums:
                highest = lowest + 1

                while highest in nums:
                    highest += 1

                best = max(best, highest - lowest)
        return best
