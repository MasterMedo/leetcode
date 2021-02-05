class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        chain = dict(zip(words, [1] * len(words)))
        for i, word in enumerate(words):
            for j in range(len(word)):
                new_word = word[:j] + word[j + 1:]
                if new_word in chain:
                    chain[word] = max(chain[word], 1 + chain[new_word])

        return max(chain.values())
