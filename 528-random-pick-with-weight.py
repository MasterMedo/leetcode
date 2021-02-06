import random
from bisect import bisect
from itertools import accumulate as acc


class Solution:
    def __init__(self, weights):
        total = sum(weights)
        self.p = list(acc(i / total for i in weights))

    def pickIndex(self) -> int:
        return bisect(self.p, random.random())
