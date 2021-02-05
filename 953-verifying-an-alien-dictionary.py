class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}
        for i, j in zip(range(len(words) - 1), range(1, len(words))):
            word1, word2 = words[i], words[j]
            for c1, c2 in zip(word1, word2):
                if order[c1] > order[c2]:
                    return False

                elif order[c1] < order[c2]:
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
