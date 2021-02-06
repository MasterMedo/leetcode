class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        reversed_vowels = (c for c in reversed(s) if c in vowels)
        return ''.join(next(reversed_vowels) if c in vowels else c for c in s)
