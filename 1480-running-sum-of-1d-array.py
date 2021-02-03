from itertools import accumulate as acc


class Solution:
    def runningSum(self, numbers: list[int]) -> list[int]:
        return list(acc(numbers))
