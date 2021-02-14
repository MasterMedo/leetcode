class Solution:
    def nextPermutation(self, arr: list[int]) -> None:
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                index = next(j for j in range(len(arr) - 1, 0, -1) if arr[j] > arr[i - 1])
                arr[index], arr[i - 1] = arr[i - 1], arr[index]
                arr[i:] = sorted(arr[i:])
                return
        arr.sort()
