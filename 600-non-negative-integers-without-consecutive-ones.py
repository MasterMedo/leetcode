class Solution:
    def fib(self, n):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)

    def findIntegers(self, n: int) -> int:
        def is_consecutive(n):
            return (n & (n << 1)) == 0

        ans = is_consecutive(n)
        while n:
            rightmost = ((n ^ (n - 1)) + 1) >> 1
            n -= rightmost
            if is_consecutive(n):
                bits = rightmost.bit_length()
                ans += self.fib(bits + 1)

        return ans
