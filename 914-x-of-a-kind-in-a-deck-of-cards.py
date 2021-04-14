from collections import Counter
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        counter = Counter(deck)
        return gcd(*counter.values()) >= 2
