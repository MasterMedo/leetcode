class Solution:
    def sortArrayByParity(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda n: n & 1)
