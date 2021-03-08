class Solution:
    def findLengthOfLCIS(self, arr: list[int]) -> int:
        if len(arr) == 0:
            return 0

        count = highest = 1
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                count += 1
                highest = max(highest, count)
            else:
                count = 1

        return highest
