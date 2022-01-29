class Solution:
    def searchInsert(self, arr: list[int], target: int) -> int:
        if target > arr[-1]:
            return len(arr)
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            n = arr[mid]
            if n > target:
                hi = mid
            elif n < target:
                lo = mid + 1
            else:
                return mid

        return lo if arr[lo] >= target else lo - 1
