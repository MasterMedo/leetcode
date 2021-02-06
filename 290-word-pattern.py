class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = dict()
        words = s.split()
        if len(words) != len(pattern):
            return False

        for word, c in zip(words, pattern):
            if c in dictionary and word != dictionary[c]:
                return False

            elif c not in dictionary:
                dictionary[c] = word

        if len(set(dictionary.values())) != len(dictionary):
            return False
        return True
