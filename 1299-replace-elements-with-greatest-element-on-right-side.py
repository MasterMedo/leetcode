class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = -1
        for i in range(len(arr) - 1, -1, -1):
            element = arr[i]
            arr[i] = maximum
            maximum = max(maximum, element)

        return arr
