class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        queue = reversed(s)
        return ''.join(c if not c.isalpha() else
                       next(q for q in queue if q.isalpha()) for c in s)
