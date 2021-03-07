from functools import cache
from collections import defaultdict


gen = iter(list(range(26)) + [-1] * 4)
table = [[chr(next(gen) + 65) for _ in range(6)] for _ in range(5)]
distances = defaultdict(int)
for r in range(5):
    for c in range(6):
        for i in range(5):
            for j in range(6):
                distances[table[r][c] + table[i][j]] = abs(r - i) + abs(c - j)


class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def dfs(first, second, i):
            if i >= len(word):
                return 0

            return min(
                dfs(word[i], second, i + 1) + distances[first + word[i]],
                dfs(word[i], first, i + 1) + distances[second + word[i]]
            )

        return dfs(word[0], '', 1)
