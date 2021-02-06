class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        d = {}
        for i, n in enumerate(arr):
            x = target - n
            if x in d:
                return [d[x], i]

            d[n] = i
