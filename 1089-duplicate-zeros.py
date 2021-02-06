class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        j = 0
        copy = arr[:]
        for i, e in enumerate(copy):
            if j >= len(arr):
                return

            arr[j] = e
            j += 1
            if j >= len(arr):
                return

            if e == 0:
                arr[j] = e
                j += 1
