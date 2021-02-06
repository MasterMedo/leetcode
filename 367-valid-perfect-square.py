class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        a = 0
        for i in range(1, 2**31, 2):
            if a > n:
                return False
            if a == n:
                return True
            a += i

        return False
