from math import gcd


class Solution:
    def gcdOfStrings(self, a: str, b: str) -> str:
        if a + b != b + a:
            return ''

        if a == b:
            return a

        x = gcd(len(a), len(b))

        if (s := a[:x]) == b[:x]:
            return s

        else:
            return ''
