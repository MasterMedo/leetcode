from itertools import permutations


class Solution:
    def permuteUnique(self, arr: list[int]) -> list[list[int]]:
        return set(permutations(arr))
