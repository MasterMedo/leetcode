from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        cnt = 0
        odd = False
        for n in counter.values():
            if n & 1:
                odd = True
                cnt += n - 1
            else:
                cnt += n

        return cnt + odd
