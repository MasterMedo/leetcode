class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = [False, {}]
        for word in wordDict:
            cur = trie
            for c in word:
                if c not in cur[1]:
                    cur[1][c] = [False, {}]
                cur = cur[1][c]
            cur[0] = True

        words = [0]
        seen = {0}
        while words:
            n = -words.pop()
            cur = trie
            for i in range(n, len(s)):
                c = s[i]
                if c not in cur[1]:
                    break

                cur = cur[1][c]
                if cur[0]:
                    if i + 1 >= len(s):
                        return True
                    if i + 1 not in seen:
                        seen.add(i+1)
                        words.append(-(i+1))

        return False
