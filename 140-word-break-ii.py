from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        @cache
        def sentences(i: int) -> list[str]:
            if i == len(s):
                return ['']

            return [s[i:j] + (' ' + suffix if suffix else suffix)
                    for j in range(i + 1, len(s) + 1) if s[i:j] in wordDict
                    for suffix in sentences(j)]

        return sentences(0)
