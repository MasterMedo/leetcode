from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        right = Counter(s)
        left = Counter()
        good = 0
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
            left[s[i]] += 1

            if len(left) == len(right):
                good += 1
        return good
