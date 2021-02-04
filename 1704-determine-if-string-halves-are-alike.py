class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        difference = 0

        for i in range(half):
            if s[i] in 'aeiouAEIOU':
                difference += 1
            if s[half + i] in 'aeiouAEIOU':
                difference -= 1

        return difference == 0
