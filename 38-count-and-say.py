from itertools import groupby
from functools import cache


class Solution:
    @cache
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return "1"

        return ''.join(f'{len(list(g))}{c}' for c, g in groupby(self.countAndSay(n - 1)))
