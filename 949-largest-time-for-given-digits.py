from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        arr.sort(reverse=True)
        for a, b, c, d in permutations(arr):
            h = a * 10 + b
            m = c * 10 + d
            if h < 24 and m < 59:
                return f'{h:02d}:{m:02d}'

        return ''
