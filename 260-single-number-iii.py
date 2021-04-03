from operator import xor
from functools import reduce


class Solution:
    def singleNumber(self, arr: list[int]) -> list[int]:
        xors = reduce(xor, arr)
        bit = xors & (-xors)
        first = reduce(xor, (n for n in arr if n & bit))
        return [first, xors ^ first]
