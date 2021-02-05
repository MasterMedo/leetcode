from collections import deque


class Solution:
    def toGoatLatin(self, s: str) -> str:
        goat_latin = []
        for i, word in enumerate(s.split(), 1):
            word = deque(word)
            if word[0] not in 'AEIOUaeiou':
                word.rotate(-1)

            word.append('m')
            word.append('a')

            for _ in range(i):
                word.append('a')

            goat_latin.append(''.join(word))

        return ' '.join(goat_latin)
