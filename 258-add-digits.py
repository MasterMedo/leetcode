class Solution:
    def addDigits(self, n: int) -> int:
        while n > 9:
            i = 0
            while n:
                n, m = divmod(n, 10)
                i += m
            n = i

        return n
