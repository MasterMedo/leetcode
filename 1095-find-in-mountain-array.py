class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        lo, hi = 0, arr.length() - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr.get(mid) < arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid

        peak = lo
        if arr.get(peak) == target:
            return peak

        lo, hi = 0, peak - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr.get(mid) < target:
                lo = mid + 1
            elif arr.get(mid) > target:
                hi = mid - 1
            else:
                return mid

        lo, hi = peak + 1, arr.length() - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr.get(mid) > target:
                lo = mid + 1
            elif arr.get(mid) < target:
                hi = mid - 1
            else:
                return mid
        return -1
