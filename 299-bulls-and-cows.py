from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        s = defaultdict(int)
        g = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s[secret[i]] += 1
                g[guess[i]] += 1
        cows = sum(min(s[digit], g[digit]) for digit in s if digit in g)
        return f'{bulls}A{cows}B'
