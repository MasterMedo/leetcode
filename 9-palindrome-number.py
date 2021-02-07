class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        d = x
        r = 0
        while d != 0:
            d, m = divmod(d, 10)
            r = r * 10 + m
        return r == x
