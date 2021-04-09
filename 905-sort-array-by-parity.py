class Solution:
    def sortArrayByParity(self, arr: list[int]) -> list[int]:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            if not arr[lo] & 1:
                lo += 1
            elif arr[hi] & 1:
                hi -= 1
            else:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1

        return arr
