from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def f(a, b):
            a, b = (a + b), (b + a)
            return (a > b) - (a < b)

        s = ''.join(sorted(map(str, nums), key=cmp_to_key(f), reverse=True)).lstrip('0')
        return s if s else '0'
