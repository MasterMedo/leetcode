class Solution:
    def search(self, arr: list[int], target: int) -> int:
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
                lo = mid
                break

        return lo if arr[lo] == target else -1
