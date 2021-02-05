from itertools import product


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        arr = []
        s = s.lower()
        alpha = sum(c.isalpha() for c in s)
        for p in product((False, True), repeat=alpha):
            p = iter(p)
            arr.append(''.join(c.upper() if c.isalpha() and next(p) else c
                               for c in s))

        return arr
