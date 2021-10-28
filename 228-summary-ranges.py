class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        arr = []
        smallest = nums[0]
        last = smallest
        for i in range(1, len(nums)):
            n = nums[i]
            if n - 1 == last:
                last = n
            else:
                arr.append(f"{smallest}->{last}" if last != smallest else f"{last}")
                smallest = n
                last = n
        arr.append(f"{smallest}->{last}" if last != smallest else f"{last}")
        return arr
