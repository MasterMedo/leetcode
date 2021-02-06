class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        N = 1
        while n:
            if n & 1:
                N *= x
            x *= x
            n >>= 1
        return N
