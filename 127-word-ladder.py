from string import ascii_lowercase
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, words: list[str]) -> int:
        def generateWords(word: str) -> list[str]:
            nonlocal words
            for i in range(len(word)):
                for c in ascii_lowercase:
                    if c != word[i]:
                        neighbour = word[:i] + c + word[i + 1:]
                        if neighbour in words:
                            yield neighbour

        words = set(words)
        seen = set([beginWord])
        visit = deque([(beginWord, 1)])
        while visit:
            word, word_cnt = visit.popleft()
            for word2 in generateWords(word):
                if word2 not in seen:
                    if word2 == endWord:
                        return word_cnt + 1
                    seen.add(word2)
                    visit.append((word2, word_cnt + 1))
        return 0
