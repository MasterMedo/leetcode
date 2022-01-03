class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n:
            n &= n - 1
            s += 1

        return s
