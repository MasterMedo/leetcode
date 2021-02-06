class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = [[None for _ in range(len(word1) + 1)]
                 for _ in range(len(word2) + 1)]

        for i in range(len(word1) + 1):
            table[0][i] = i
        for i in range(len(word2) + 1):
            table[i][0] = i

        for i, c1 in enumerate(word1, 1):
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    table[j][i] = table[j-1][i-1]
                else:
                    table[j][i] = min(
                        table[j-1][i-1],
                        table[j-1][i],
                        table[j][i-1],
                    ) + 1
        return table[len(word2)][len(word1)]
