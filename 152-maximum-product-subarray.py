class Solution:
    def maxProduct(self, arr: list[int]) -> int:
        best = hi = lo = arr[0]
        for i in range(1, len(arr)):
            n = arr[i]
            if n < 0:
                hi, lo = lo, hi
            hi = max(n, hi * n)
            lo = min(n, lo * n)
            best = max(best, hi)
        return best
