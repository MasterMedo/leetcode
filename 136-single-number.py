from operator import xor
from functools import reduce


class Solution:
    def singleNumber(self, arr: list[int]) -> int:
        return reduce(xor, arr)
