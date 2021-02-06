from itertools import groupby, zip_longest


class Solution:
    def expressiveWords(self, word: str, words: list[str]) -> int:
        groups = [(k, len(list(g))) for k, g in groupby(word)]

        sol = 0
        for word in words:
            for g1, g2 in zip_longest(groupby(word), groups, fillvalue='.'):
                if g1[0] != g2[0]\
                        or (g2[1] >= 3 and len(list(g1[1])) > g2[1])\
                        or (g2[1] < 3 and len(list(g1[1])) != g2[1]):
                    break
            else:
                sol += 1

        return sol
