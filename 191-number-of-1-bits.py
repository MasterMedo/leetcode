class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 1
        s = 0
        while i <= n:
            if i & n:
                s += 1
            i *= 2

        return s
