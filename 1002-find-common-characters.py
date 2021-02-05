from math import inf


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = [inf] * 26
        for word in words:
            alphabet = [0] * 26
            for c in word:
                alphabet[ord(c) - 97] += 1

            common = [min(a, b) for a, b in zip(common, alphabet)]

        return list(''.join(chr(i + 97) * common[i]
                            for i in range(26) if common[i] != inf))
