from random import sample


class Solution:
    def repeatedNTimes(self, arr: list[int]) -> int:
        return next(a for a, b in (sample(arr, 2) for _ in iter(int, 1)) if a == b)
