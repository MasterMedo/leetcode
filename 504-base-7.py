class Solution:
    def convertToBase7(self, n: int) -> str:
        sign = '-' if n < 0 else ''
        n = abs(n)
        base7 = []
        while n != 0:
            n, m = divmod(n, 7)
            base7.append(str(m))

        base7 = ''.join(reversed(base7))
        return sign + (base7 if base7 else '0')
