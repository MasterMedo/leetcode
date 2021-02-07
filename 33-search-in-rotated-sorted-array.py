from bisect import bisect_left


class Solution:
    def search(self, arr: list[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid

        if target > arr[-1]:
            lo = 0
        else:
            hi = len(arr) - 1

        index = bisect_left(arr, target, lo=lo, hi=hi)
        return index if arr[index] == target else -1
