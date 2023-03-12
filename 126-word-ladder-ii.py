from string import ascii_lowercase
from collections import defaultdict, deque
from functools import cache


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, words: list[str]
    ) -> list[list[str]]:
        @cache
        def generateWords(word: str) -> list[str]:
            nonlocal words
            arr = []
            for i in range(len(word)):
                for c in ascii_lowercase:
                    if c != word[i]:
                        neighbour = word[:i] + c + word[i + 1:]
                        if neighbour in words:
                            arr.append(neighbour)
            return arr

        def bfs():
            nonlocal best
            seen = set([beginWord])
            visit = deque([(beginWord, 1)])
            while visit:
                word, word_cnt = visit.popleft()
                best[word] = word_cnt
                for word2 in generateWords(word):
                    if word2 not in seen:
                        if word2 == endWord:
                            return word_cnt + 1
                        seen.add(word2)
                        visit.append((word2, word_cnt + 1))
            return 0

        @cache
        def dfs(word, path_length) -> list[list[str]]:
            nonlocal min_path, best
            if path_length > min_path:
                return

            if word == endWord:
                return [[endWord]]

            paths = []
            for word2 in generateWords(word):
                if best[word2] >= path_length + 1:
                    best[word2] = path_length + 1
                    if subpaths := dfs(word2, path_length + 1):
                        for path in subpaths:
                            paths.append([word] + path)

            return paths

        words = set(words)
        best = defaultdict(lambda: float("inf"))
        min_path = bfs()
        print(min_path)
        return dfs(beginWord, 1)
