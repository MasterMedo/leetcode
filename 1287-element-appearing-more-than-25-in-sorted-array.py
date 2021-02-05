class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = 1
        m = len(arr) / 4
        current = arr[0]
        for i in range(1, len(arr)):
            if arr[i] == current:
                n += 1
            else:
                current = arr[i]
                n = 1
            if n > m:
                break

        return current
