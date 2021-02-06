class Solution:
    def reverse(self, x: int) -> int:
        n = int(str(abs(x))[::-1]) * pow(-1, x < 0)
        return n if -pow(2, 31) <= n <= pow(2, 31) - 1 else 0
