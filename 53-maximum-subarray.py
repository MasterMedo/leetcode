class Solution:
    def maxSubArray(self, arr: list[int]) -> int:
        best = arr[0]
        m = arr[0]
        for i in range(1, len(arr)):
            n = arr[i]
            m = max(n, m + n)
            best = max(best, m)
        return best
