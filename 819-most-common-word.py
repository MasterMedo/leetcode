import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = []
        banned = set(banned)
        for word in re.findall(r'(\w+)', paragraph):
            word = word.lower()
            if word not in banned:
                words.append(word)

        return Counter(words).most_common(1)[0][0]
