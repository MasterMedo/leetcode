class Solution:
    def candy(self, arr: list[int]) -> int:
        if not arr:
            return 0

        hi = [0]*len(arr)
        lo = [0]*len(arr)
        rise = 0
        last = arr[0]
        for i in range(len(arr)):
            if arr[i] > last:
                rise += 1
            else:
                rise = 0
            hi[i] = rise
            last = arr[i]

        rise = 0
        last = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > last:
                rise += 1
            else:
                rise = 0
            lo[i] = rise
            last = arr[i]

        return sum(max(a, b) + 1 for a, b in zip(lo, hi))
