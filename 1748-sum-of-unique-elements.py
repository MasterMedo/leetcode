from collections import Counter


class Solution:
    def sumOfUnique(self, arr: list[int]) -> int:
        return sum(n for n, i in Counter(arr).items() if i == 1)
