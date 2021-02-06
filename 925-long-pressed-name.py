from itertools import groupby, zip_longest


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        for g1, g2 in zip_longest(groupby(name), groupby(typed), fillvalue='#'):
            if g1[0] != g2[0] or len(list(g1[1])) > len(list(g2[1])):
                return False
        return True
