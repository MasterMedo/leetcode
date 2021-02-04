class Solution:
    def sumZero(self, n: int) -> list[int]:
        return range(1 - n, n, 2)
